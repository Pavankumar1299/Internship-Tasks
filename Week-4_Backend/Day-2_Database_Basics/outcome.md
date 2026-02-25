**Expected Outcome**
The Students table should be queried successfully using the WHERE clause. 
Only those records should be displayed where: 
The student’s age is greater than or equal to 25 
The student’s name ends with the specified character (using LIKE '%n') 
The output should contain filtered rows matching both conditions 
 
**Actual Outcome**
The SQL query executed without errors in MySQL. 
The result set displayed only the students who: 
Are aged 25 or above 
Have names ending with the given character 
Records that did not meet the conditions were excluded from the result.