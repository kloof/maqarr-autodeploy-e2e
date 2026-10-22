package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/go-chi/chi/v5"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8000"
	}
	router := chi.NewRouter()
	router.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/plain; charset=utf-8")
		fmt.Fprintln(w, "maqarr-auto-e2e:go:recovery")
	})
	log.Printf("maqarr-auto-e2e:go:recovery ready :%s", port)
	log.Fatal(http.ListenAndServe(":"+port, router))
}
