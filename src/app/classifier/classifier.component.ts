import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'

import { ClassifierService } from './classifier.service'

@Component({
  selector: 'app-classifier',
  templateUrl: './classifier.component.html',
  styleUrls: ['./classifier.component.css']
})


export class ClassifierComponent implements OnInit {

  images: {id: number, img: string}[] = [];
  httpClient;
  selected_image = null;
  viewing_image: {id: number, images: { description: string, img: string }[] } | null = null;
  selected_result_image: { description: string, img: string } | null = null;


  constructor(service: ClassifierService, httpClient: HttpClient) {
    this.httpClient = httpClient;
    service.getImages(httpClient).subscribe(res => {
        let records: {id: number, img: string}[] = [];
        let json_images = JSON.parse(JSON.stringify(res))["images"];
        for(let id in json_images){
          let img = json_images[id];
          records.push({id: Number(id), img: img});
        }
        this.images = records;
    });
  }

  onFileSelected(event: any){
    this.selected_image = event.target.files[0];
  }

  uploadImage(){
    if (this.selected_image){
      const fd = new FormData();
      fd.append('image', this.selected_image, (<File>this.selected_image).name);
      fd.append('action', 'process');
      this.httpClient.post('http://127.0.0.1:5000', fd)
        .subscribe(res =>{
              window.location.reload();
        });
    }
  }

  viewImage(id: number){
    this.viewing_image = null;
    this.selected_result_image = null;
    this.httpClient.get("http://127.0.0.1:5000/GetResult?id="+id)
      .subscribe(res =>{
        let json_response = JSON.parse(JSON.stringify(res));
        let json_images = json_response["images"];
        let images = [];
        for (let index in json_images){
          let json_image = json_images[index];
          images.push({ description: json_image["description"], img: json_image["img"] });
        }
        console.log(images);
        this.viewing_image = { id: id, images: images } ;
      });
  }

  view_result(image: { description: string, img: string }){
    this.selected_result_image = image;
  }

  ngOnInit(): void {}

}
