
CREATE TABLE name_table (
  StudentID TEXT PRIMARY KEY,
  Name TEXT NOT NULL
);

CREATE TABLE mark_table (
  StudentID TEXT PRIMARY KEY,
  Total_marks INTEGER NOT NULL
);

INSERT INTO name_table VALUES ("V001", 'Abe');
INSERT INTO name_table VALUES ("V002", 'Abhay');
INSERT INTO name_table VALUES ("V003", 'Acelin');
INSERT INTO name_table VALUES ("V004", 'Adelphos');


INSERT INTO mark_table VALUES ("V001", 95);
INSERT INTO mark_table VALUES ("V002", 80);
INSERT INTO mark_table VALUES ("V003", 74);
INSERT INTO mark_table VALUES ("V004", 81);

SELECT name_table.StudentID, Name FROM name_table, mark_table
WHERE  name_table.StudentID = mark_table.StudentID AND Total_marks > (
        SELECT Total_marks FROM name_table, mark_table
        WHERE name_table.StudentID = mark_table.StudentID  AND name_table.StudentID = 'V002');
    

