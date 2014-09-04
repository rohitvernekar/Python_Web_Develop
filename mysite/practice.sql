PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "books_publisher" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL,
    "address" varchar(50) NOT NULL,
    "city" varchar(60) NOT NULL,
    "state_province" varchar(30) NOT NULL,
    "country" varchar(50) NOT NULL,
    "website" varchar(200) NOT NULL
);
INSERT INTO "books_publisher" VALUES(1,'Rohit','Ashok nagar nippani','Bangalore','Karnataka','India','http://www.gmail.com/');
INSERT INTO "books_publisher" VALUES(2,'Rahul','Ashok Nagar','Belgaum','maharastra','India','http://www.google.com/');
INSERT INTO "books_publisher" VALUES(3,'Rushikesh','Pande quaters','Bangalore','Karnataka','India','http://www.gmail.com/');
CREATE TABLE "books_author" (
    "id" integer NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(40) NOT NULL,
    "email" varchar(75) NOT NULL
);
CREATE TABLE "books_book_authors" (
    "id" integer NOT NULL PRIMARY KEY,
    "book_id" integer NOT NULL,
    "author_id" integer NOT NULL REFERENCES "books_author" ("id"),
    UNIQUE ("book_id", "author_id")
);
CREATE TABLE "books_book" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(100) NOT NULL,
    "publisher_id" integer NOT NULL REFERENCES "books_publisher" ("id"),
    "publication_date" date NOT NULL
);
CREATE INDEX "books_book_authors_752eb95b" ON "books_book_authors" ("book_id");
CREATE INDEX "books_book_authors_337b96ff" ON "books_book_authors" ("author_id");
CREATE INDEX "books_book_22dd9c39" ON "books_book" ("publisher_id");
COMMIT;
