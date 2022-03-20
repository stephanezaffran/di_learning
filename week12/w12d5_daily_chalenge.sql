Q1. What will be the OUTPUT of the following statement?      answere = 0

    SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

===> equal to ---->

 SELECT *
    FROM FirstTab AS ft WHERE ft.id != NULL

count ft
1    3   <-------- error why ?

====================================================================================

Q2. What will be the OUTPUT of the following statement?     answere = 2

    SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
    ===> equal to ---->

 SELECT *
    FROM FirstTab AS ft WHERE ft.id != 5


count ft
1   3   <------ error the null doesn't counted ?

=======================================================================================

Q3. What will be the OUTPUT of the following statement?     answere = 0

    SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

 SELECT *
    FROM FirstTab AS ft WHERE ft.id != (NULL,5)


    count ft
1   2   <------ error the null doesn't counted ?


==========================================================================================

Q4. What will be the OUTPUT of the following statement?    same as Q2 for this case

    SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )