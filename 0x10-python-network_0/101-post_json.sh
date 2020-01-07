#!/bin/bash
#script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sh "Content-Type: application/jason" -X post "@$2""$1"
