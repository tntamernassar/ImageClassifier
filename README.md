# TextClassifier

web-based system to define main text, text lines, and words in a page.
Using this web application, you can upload image containing text. 
And get three versions of the image : 
- image defining words
- image defining text lines
- image defining main text


## System Architecture

![image](https://user-images.githubusercontent.com/26690099/159124325-f57ebdde-9916-40f1-a8a9-485986acd1c0.png)

## Image Processing

To extract the words from a certain image, we used an external process called "pytesseract" which we treated as a black box
that takes in out input image, processes it into readable data stored in a list, which we then iterate over and get our 
desired values which are the points of the rectangle which covers each word in the photo (We also check certain conditions such
as if its not the first value we read and if its size is 12, otherwise it means its not a complete data block or a corrupted one).

To extract the text lines from a certain image, we converted the image into gray scale, applied some threshold, we then detect
the structure shape by choosing a proper kernel (what we thought would fit for most images), then by using a dilution morphology we 
to 'blur' a text in a line, find the identified contours and by that we get the bounding rectangle of each single text line.

To extract the main text from a certain image, we use almost the same method as in extracting text lines, but before we dilate,
we increase the kernel size of the structure element to (15, 15) to identify larger text chunks and applying the same process on them.

## Usage

1. Run dev server (See Development server section), and navigate to http://127.0.0.1:5000

2. Select image from your machine and click upload

![image](https://user-images.githubusercontent.com/26690099/159124151-71358fb0-fc00-4a3e-9034-7a0299039198.png)



3. Click on View Image

![image](https://user-images.githubusercontent.com/26690099/159124171-a419da94-374a-48b6-b3c6-71500f2e7d4a.png)



2. Navigate through the menu to view result images

![image](https://user-images.githubusercontent.com/26690099/159124177-51ceb7da-1c5d-449d-a997-f231d96ed8d8.png)




## Original Image

![image](https://user-images.githubusercontent.com/26690099/159124261-46232769-96f9-4f70-b413-72f41bc94c46.png)



## Defined Main Text
![image](https://user-images.githubusercontent.com/26690099/159124266-a431df1e-876b-4988-8e7a-11c0642cfeee.png)


## Defined words
![image](https://user-images.githubusercontent.com/26690099/159124268-03fb3478-12f8-45eb-9b62-b3bec37087af.png)


## Defined Text Lines
![image](https://user-images.githubusercontent.com/26690099/159124269-2e51718a-73bc-498b-a193-ea3f57d1bb43.png)




## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.
