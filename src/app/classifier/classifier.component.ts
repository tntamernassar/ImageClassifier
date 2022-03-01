import { Component, OnInit } from '@angular/core';

import { ClassifierService } from './classifier.service'

@Component({
  selector: 'app-classifier',
  templateUrl: './classifier.component.html',
  styleUrls: ['./classifier.component.css']
})
export class ClassifierComponent implements OnInit {

  images;

  constructor(service: ClassifierService) {
    this.images = service.getImages();
  }

  ngOnInit(): void {

  }

}
