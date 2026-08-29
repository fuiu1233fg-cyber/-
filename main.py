package main

import (
	"fmt"
	"net/http"
	"math/rand"
	"time"
)

// دالة لتوليد رابط فريد ومميز لكل هدف
func generatePayloadLink(w http.ResponseWriter, r *http.Request) {
	rand.Seed(time.Now().UnixNano())
	token := rand.Int63()
	
	link := fmt.Sprintf("http://192.168.1.100:8080/payload/download?token=%d", token)
	
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, "<h2>رابط التحميل المخصص:</h2><a href='%s'>%s</a>", link, link)
}

func main() {
	http.HandleFunc("/generate", generatePayloadLink)
	http.ListenAndServe(":8080", nil)
}



