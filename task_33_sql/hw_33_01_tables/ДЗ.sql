--1.1.����������� ���� ���������� �� ������� �� ���������� � ��������;
--SELECT *
--FROM Students

--SELECT *
--FROM Achievements

--SELECT *
--FROM Subjects

--SELECT LastName, FirstName, Assesment
--FROM Students AS S, Achievements AS AC
--WHERE S.id = AC.id


--1.2.����������� ��� ���� ���������;
--SELECT FirstName + ' ' + LastName AS FullName
--FROM Students


--1.3.����������� ���� ������� ������;
--SELECT id, AVG(Assesment) AS average_grade
--FROM Achievements
--GROUP BY id;

--1.4.�������� ��� ���� ��������� � ����������� �������, ������, ��� ���������;
--SELECT LastName, Assesment
--FROM Students AS S, Achievements AS ACH
--WHERE S.id = ACH.id
--GROUP BY LastName, Assesment
--HAVING AVG(Assesment) < 8
--ORDER BY LastName 


--1.5.�������� ������ ���������. �������� ����� ������ ���� �����������;
--SELECT DISTINCT Countries
--FROM Students


--1.6.�������� ������ ���������. �������� ������� ������ ���� �����������;
--SELECT DISTINCT Cities
--FROM Students


--1.7.�������� �������� ���� ��������� � ������������ �������� ��������. �������� ��������� ������ ���� �����������.
--SELECT DISTINCT Subjectname, Assesment
--FROM Subjects AS S, Achievements AS A
--WHERE S.id = A.SubjectId
--GROUP BY Subjectname, Assesment
--HAVING Assesment = MIN(Assesment)





--2.1.�������� ��� ���� ��������� � ����������� ������� � ��������� ���������;
--SELECT S.FirstName, S.LastName
--FROM Students AS S
--JOIN Achievements AS ACH ON S.id = ACH.StudentId
--WHERE ACH.Assesment = (
    --SELECT MIN(Assesment)
    --FROM Achievements
    --WHERE Assesment BETWEEN 10 AND 13
--)


--2.2. �������� ���������� � ���������, ������� ����������� 20 ���;
--SELECT *
--FROM Students AS S
--WHERE DATEDIFF(YEAR, S.BirthDate, GETDATE()) >= 20;


--2.3. �������� ���������� � ��������� � ��������� � ��������� ���������;
--SELECT *
--FROM Students AS S
--WHERE DATEDIFF(YEAR, S.BirthDate, GETDATE()) BETWEEN 20 AND 27;


--2.4. �������� ���������� � ��������� � ���������� ������. ��������, �������� ��������� � ������ �����
--SELECT *
--FROM Students
--WHERE FirstName like 'Oliver%'


--2.5.�������� ���������� � ���������, � ���� ������ ����������� ��� �������;
--SELECT * 
--FROM Students 
--WHERE id LIKE '%13%';


--2.6. �������� ����������� ������ ���������, ������������ � ���������� �����.
--SELECT FirstName, LastName, Email
--FROM Students
--WHERE FirstName like 'J%'





--3.1. �������� ����������� ������� ������ �� ���� ���������;
--SELECT MIN(average_grade) AS min_average_grade
--FROM (
    --SELECT S.id, AVG(Assesment) AS average_grade
    --FROM Students AS S, Achievements AS ACH
    --GROUP BY S.id
--) AS student_averages;

--3.2. �������� ������������ ������� ������ �� ���� ���������;
--SELECT MAX(average_grade) AS max_average_grade
--FROM (
    --SELECT S.id, AVG(Assesment) AS average_grade
    --FROM Students AS S, Achievements AS ACH
    --GROUP BY S.id
--) AS student_averages;


--3.3. �������� ���������� ������� ���������. ����� ���������� �������� ������ � ���������� ��������� �� ����� ������;
--SELECT Cities, COUNT(Cities) as [num of students]
--FROM Students
--GROUP BY Cities


--3.4. �������� ���������� ����� ���������. ����� ���������� �������� ������ � ���������� ��������� �� ���� ������;
--SELECT Countries, COUNT(Countries) as [num of students]
--FROM Students
--GROUP BY Countries
--ORDER BY [num of students] DESC;

--3.5. �������� ���������� ���������, � ������� ����������� ������� ������ �� Discrete Math;



--3.6. �������� ���������� ���������, � ������� ������������ ������� ������ �� Discrete Math;



--3.7. �������� ���������� ��������� � ������ ������;
--SELECT GroupName, COUNT(*) AS student_count
--FROM Groups AS G, Students AS S
--WHERE G.Id = S.GroupId
--GROUP BY GroupName;


--3.8. �������� ������� ������ �� ������.
--SELECT GroupName, AVG(Assesment) AS middel_count
--FROM Groups AS G, Students AS S, Achievements AS ACH
--WHERE ACH.id = S.id AND G.Id = S.id 
--GROUP BY GroupName;
