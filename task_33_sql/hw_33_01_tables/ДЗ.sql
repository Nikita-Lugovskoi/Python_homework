--1.1.Отображение всей информации из таблицы со студентами и оценками;
--SELECT *
--FROM Students

--SELECT *
--FROM Achievements

--SELECT *
--FROM Subjects

--SELECT LastName, FirstName, Assesment
--FROM Students AS S, Achievements AS AC
--WHERE S.id = AC.id


--1.2.Отображение ФИО всех студентов;
--SELECT FirstName + ' ' + LastName AS FullName
--FROM Students


--1.3.Отображение всех средних оценок;
--SELECT id, AVG(Assesment) AS average_grade
--FROM Achievements
--GROUP BY id;

--1.4.Показать ФИО всех студентов с минимальной оценкой, больше, чем указанная;
--SELECT LastName, Assesment
--FROM Students AS S, Achievements AS ACH
--WHERE S.id = ACH.id
--GROUP BY LastName, Assesment
--HAVING AVG(Assesment) < 8
--ORDER BY LastName 


--1.5.Показать страны студентов. Названия стран должны быть уникальными;
--SELECT DISTINCT Countries
--FROM Students


--1.6.Показать города студентов. Названия городов должны быть уникальными;
--SELECT DISTINCT Cities
--FROM Students


--1.7.Показать название всех предметов с минимальными средними оценками. Названия предметов должны быть уникальными.
--SELECT DISTINCT Subjectname, Assesment
--FROM Subjects AS S, Achievements AS A
--WHERE S.id = A.SubjectId
--GROUP BY Subjectname, Assesment
--HAVING Assesment = MIN(Assesment)





--2.1.Показать ФИО всех студентов с минимальной оценкой в указанном диапазоне;
--SELECT S.FirstName, S.LastName
--FROM Students AS S
--JOIN Achievements AS ACH ON S.id = ACH.StudentId
--WHERE ACH.Assesment = (
    --SELECT MIN(Assesment)
    --FROM Achievements
    --WHERE Assesment BETWEEN 10 AND 13
--)


--2.2. Показать информацию о студентах, которым исполнилось 20 лет;
--SELECT *
--FROM Students AS S
--WHERE DATEDIFF(YEAR, S.BirthDate, GETDATE()) >= 20;


--2.3. Показать информацию о студентах с возрастом в указанном диапазоне;
--SELECT *
--FROM Students AS S
--WHERE DATEDIFF(YEAR, S.BirthDate, GETDATE()) BETWEEN 20 AND 27;


--2.4. Показать информацию о студентах с конкретным именем. Например, показать студентов с именем Борис
--SELECT *
--FROM Students
--WHERE FirstName like 'Oliver%'


--2.5.Показать информацию о студентах, в чьем номере встречаются три семерки;
--SELECT * 
--FROM Students 
--WHERE id LIKE '%13%';


--2.6. Показать электронные адреса студентов, начинающихся с конкретной буквы.
--SELECT FirstName, LastName, Email
--FROM Students
--WHERE FirstName like 'J%'





--3.1. Показать минимальную среднюю оценку по всем студентам;
--SELECT MIN(average_grade) AS min_average_grade
--FROM (
    --SELECT S.id, AVG(Assesment) AS average_grade
    --FROM Students AS S, Achievements AS ACH
    --GROUP BY S.id
--) AS student_averages;

--3.2. Показать максимальную среднюю оценку по всем студентам;
--SELECT MAX(average_grade) AS max_average_grade
--FROM (
    --SELECT S.id, AVG(Assesment) AS average_grade
    --FROM Students AS S, Achievements AS ACH
    --GROUP BY S.id
--) AS student_averages;


--3.3. Показать статистику городов студентов. Нужно отображать название города и количество студентов из этого города;
--SELECT Cities, COUNT(Cities) as [num of students]
--FROM Students
--GROUP BY Cities


--3.4. Показать статистику стран студентов. Нужно отображать название страны и количество студентов из этой страны;
--SELECT Countries, COUNT(Countries) as [num of students]
--FROM Students
--GROUP BY Countries
--ORDER BY [num of students] DESC;

--3.5. Показать количество студентов, у которых минимальная средняя оценка по Discrete Math;



--3.6. Показать количество студентов, у которых максимальная средняя оценка по Discrete Math;



--3.7. Показать количество студентов в каждой группе;
--SELECT GroupName, COUNT(*) AS student_count
--FROM Groups AS G, Students AS S
--WHERE G.Id = S.GroupId
--GROUP BY GroupName;


--3.8. Показать среднюю оценку по группе.
--SELECT GroupName, AVG(Assesment) AS middel_count
--FROM Groups AS G, Students AS S, Achievements AS ACH
--WHERE ACH.id = S.id AND G.Id = S.id 
--GROUP BY GroupName;
