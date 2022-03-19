import { HttpClient } from '@angular/common/http'

export class ClassifierService{

  /**
    Send HTTP Request to get the images
  **/
  getImages(httpClient: HttpClient) {
    return httpClient.get("http://127.0.0.1:5000/GetImages");
  }

}
