from docx import Document
import json

doc = Document('movies3.docx')

#use this logic to initially parse the original word file until it returns a reasonable line by line output
def getText(filename):
    #Create a raw list of movies from first parse
    moviesList = []
    #read every paragraph line
    for word in filename.paragraphs:
        #Check these corner cases for bad delimiters and break them into new objects(strings) in the list
        if "___" in word.text:
            continue
        if "  " in word.text:
            for wordSplit in word.text.split("  "):
                moviesList.append(wordSplit)
        if "\t" in word.text:
            for wordSplit in word.text.split("\t"):
                moviesList.append(wordSplit)
        if "\n" in word.text:
            for wordSplit in word.text.split("\n"):
                moviesList.append(wordSplit)
        else:
            #Wow we almost surely got a good result probably maybe...
            moviesList.append(word.text)
    #Now a final list to clean and return
    moviesCleanList = []
    for movie in moviesList:
        # Just remove the whitespacing in front and back of the string...
        movie = movie.strip()
        if movie:
            #And if it still has text (isn't empty), then add it to the final list
            moviesCleanList.append(movie)
    return moviesCleanList
#Print a prettified list, but realistically you'll want to save this to its own file to parse later
#print(json.dumps(getText(doc), indent=2))
cleanedMovies = json.dumps(getText(doc), indent=2)
with open ('cleanedmovies.json','w') as outfile:
    json.dump(cleanedMovies,outfile)