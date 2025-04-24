def exists_doctors(table_name):
    QUERY = fr"""SELECT Surname, Name, Salary, Premium
                    FROM {table_name}
                    WHERE EXISTS(SELECT * 
                                    FROM DoctorsExaminations 
                                    WHERE DoctorsExaminations.DoctorId = Doctors.id);"""
    return QUERY

def exists_doctor_for_ward(table_name, Ward_Id):
    QUERY = fr"""SELECT Surname, Name, Salary, Premium
                    FROM {table_name}
                    WHERE Id = ANY(SELECT DoctorId 
                                        FROM DoctorsExaminations 
                                        WHERE WardId = {Ward_Id})"""
    return QUERY

def exists_doctor_for_exam_time(table_name, StartTime, EndTime):
    QUERY = fr"""SELECT Surname, Name, Salary, Premium
                    FROM {table_name}
                    WHERE Id = SOME(SELECT DoctorId 
                                    FROM DoctorsExaminations 
                                    WHERE StartTime <= '{StartTime}' AND EndTime >= '{EndTime}');"""
    return QUERY

def select_doctor_for_all_wardId():
    QUERY = fr"""SELECT Surname, Name, WardId
                    FROM Doctors AS D, DoctorsExaminations AS DOE
                    WHERE DoctorId = D.id AND WardId > ALL(SELECT AVG(WardId) 
                                                            FROM DoctorsExaminations 
                                                            GROUP BY DoctorId);"""
    return QUERY

def select_union_doctors(table_name):
    QUERY = fr"""SELECT Surname + ' ' + Name + '(1)' AS [Fullname], Salary
                    From {table_name}
                    WHERE Salary > '55000'
                    Union
                    SELECT Surname + ' ' + Name + '(2)' AS [Fullname], Salary
                        From {table_name}
                        WHERE Salary > '69000'
                        ORDER BY Salary DESC"""
    return QUERY


def select_all_union_doctors(table_name):
    QUERY = fr"""SELECT 'BAD' AS [Result], COUNT(*) AS [Number_of_Doctors]
                    FROM {table_name}
                    WHERE Premium < 4000
                    UNION ALL
                    SELECT 'NORM', COUNT(*)
                        FROM {table_name}
                        WHERE Premium BETWEEN 4000 AND 4999
                        UNION ALL
                        SELECT 'BETTER', COUNT(*) 
                            FROM {table_name}
                            WHERE Premium BETWEEN 5000 AND 5999
                            UNION ALL
                            SELECT 'GOOD', COUNT(*) 
                                FROM {table_name}
                                WHERE Premium BETWEEN 6000 AND 6999
                                UNION ALL
                                SELECT 'BEST', COUNT(*)
                                    FROM {table_name}
                                    WHERE Premium BETWEEN 7000 AND 7999"""
    return QUERY


def join_info_about_doctors():
    QUERY = fr"""SELECT Surname, Doctors.Name AS [Name], W.Name AS [Ward], DEP.Name AS [Departament]
                    FROM Doctors JOIN DoctorsExaminations ON Doctors.id = DoctorsExaminations.DoctorId
                                 JOIN Wards AS W ON DoctorsExaminations.WardId = W.id
                                 JOIN Departments AS DEP ON W.DepartmentId = DEP.id"""
    return QUERY