-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


-- Crowdfunding ERD
CREATE TABLE "Campaign" (
    -- Crowdfunding (CF) ID "Primary Keys, INT"
    "cf_id" INT   NOT NULL,
    -- Contacts ID "Foreign Keys, Share unique keys with Contacts.contact_id one TO one"
    "contact_id" INT   NOT NULL,
    -- Company Name "A VARIABLE length string e.g. Baldwin, Riley and Jackson"
    "company_name" VARCHAR(255)   NOT NULL,
    -- CF Description "A VARIABLE length string e.g. Pre-emptive tertiary standardization"
    "description" VARCHAR(255)   NOT NULL,
    -- CF Goal "A Float e.g. 100.0"
    "goal" DECIMAL   NOT NULL,
    -- CF Pledged "A Float e.g. 0.0"
    "pledged" DECIMAL   NOT NULL,
    -- CF Outcome "A VARIABLE length string e.g. failed or successful"
    "outcome" VARCHAR(255)   NOT NULL,
    -- CF Backers Count "INT"
    "backers_count" INT   NOT NULL,
    -- Country "A CHAR e.g. US"
    "country" CHAR(2)   NOT NULL,
    -- Currency "A CHAR e.g. USD"
    "currency" CHAR(3)   NOT NULL,
    -- Currency "A CHAR e.g. USD"
    "launched_date" DATE   NOT NULL,
    -- Currency "A CHAR e.g. USD"
    "end_date" DATE   NOT NULL,
    -- Category ID "Foreign Keys, Share unique keys with Category.category_id many TO one"
    "category_id" CHAR(4)   NOT NULL,
    -- Subcategory ID "Foreign Keys, Share unique keys with Subcategory.subcategory_id many TO one"
    "subcategory_id" VARCHAR(10)   NOT NULL,
    CONSTRAINT "pk_Campaign" PRIMARY KEY (
        "cf_id"
     )
);

CREATE TABLE "Contacts" (
    -- Contacts ID "Primary Keys, INT"
    "contact_id" INT   NOT NULL,
    -- Contacts First Name "A VARIABLE length string e.g. Cecilia"
    "first_name" VARCHAR(255)   NOT NULL,
    -- Contacts Last Name "A VARIABLE length string e.g. Velasco"
    "last_name" VARCHAR(255)   NOT NULL,
    -- Contacts Email "A VARIABLE length string e.g. cecilia.velasco@rodrigues.fr"
    "email" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Contacts" PRIMARY KEY (
        "contact_id"
     )
);

CREATE TABLE "Category" (
    -- Category ID "Primary Keys"
    "category_id" CHAR(4)   NOT NULL,
    -- Category "A VARIABLE length string e.g. technology"
    "category" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Category" PRIMARY KEY (
        "category_id"
     )
);

CREATE TABLE "Subcategory" (
    -- Subcategory ID "Primary Keys"
    "subcategory_id" VARCHAR(10)   NOT NULL,
    -- Subcategory "A VARIABLE length string e.g. web"
    "subcategory" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Subcategory" PRIMARY KEY (
        "subcategory_id"
     )
);

ALTER TABLE "Campaign" ADD CONSTRAINT "fk_Campaign_contact_id" FOREIGN KEY("contact_id")
REFERENCES "Contacts" ("contact_id");

ALTER TABLE "Campaign" ADD CONSTRAINT "fk_Campaign_category_id" FOREIGN KEY("category_id")
REFERENCES "Category" ("category_id");

ALTER TABLE "Campaign" ADD CONSTRAINT "fk_Campaign_subcategory_id" FOREIGN KEY("subcategory_id")
REFERENCES "Subcategory" ("subcategory_id");

