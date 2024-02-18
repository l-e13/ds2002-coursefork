#!/bin/bash

clear
echo "Let's build a mad-lib!"

# Collecting words
read -p "1. Please give me an adjective: " ADJ1
read -p "2. Please give me a verb: " VERB1
read -p "3. Please give me an adverb: " ADVERB1
read -p "4. Please give me a food: " FOOD
read -p "5. Please give me a city name: " CITY
read -p "6. Please give me another verb: " VERB2
read -p "7. Please give me another adjective: " ADJ2
read -p "8. Please give me an animal: " ANIMAL

# Creating the story
echo "Once upon a time there was a city called $CITY."
echo "In $CITY, there lived a $ADJ1 chef who loved to cook $FOOD."
echo "It was the chef's birthday so he wanted to get a pet $ANIMAL."
echo "So he went to the pet store and saw a $ADJ2 $ANIMAL running around in its cage."
echo "He knew he wanted it so he bought it and took it home."
echo "He was playing with his new $ANIMAL when he noticed that the $ANIMAL liked to $VERB1 $ADVERB1.This made him laugh."
echo "To add more adventure to his birthday, the chef wanted to go $VERB2, so he did."
echo "After his long day, the chef was very tired so he went to sleep and dreamed about his $ANIMAL." 
echo "The end."

