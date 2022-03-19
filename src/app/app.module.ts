import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from "@angular/forms"
import { HttpClientModule } from '@angular/common/http'

import { AppComponent } from './app.component';
import { ClassifierComponent } from './classifier/classifier.component';
import { ClassifierService } from './classifier/classifier.service';

@NgModule({
  declarations: [
    AppComponent,
    ClassifierComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    ClassifierService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
