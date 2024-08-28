from django.shortcuts import render

# Create your views here.
def hello_world():
    print("Hello world")

hello_world()

def sort_textbooks():
    #an array of textbooks
    textbooks = ["Introduction to java", "data structures and algorithms in java"]
    for x in textbooks:
        print(x)
        # for y in (x-1):
            # pass

sort_textbooks()