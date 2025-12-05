package app

import (
	"belajar-golang-restful-api/helper"
	"database/sql"
	"time"
)

func NewDB() *sql.DB {
	db, err := sql.Open("mysql", "root:1221425sql@tcp(localhost:3306)/belajar_golang_restful_api")
	helper.PanicIfError(err)

	// set maksimum konection
	db.SetMaxOpenConns(25)
	db.SetMaxIdleConns(5)
	db.SetConnMaxLifetime(time.Hour)
	db.SetConnMaxIdleTime(10 * time.Minute)
	return db
}
