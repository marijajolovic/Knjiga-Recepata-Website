alert("Upozorenje! Ako nastavite dalje mozda postanete gladni! Nastavite po sopstvenom riziku ! ☺")
let gallery = document.getElementById('gallaryId')
let slika = document.getElementById('slika')
let images = []

function loaduj(){
    loadData('xmls/breakie_dishes.xml')
    loadData('xmls/dinner_dishes.xml')
    loadData('xmls/lunch_dishes.xml')

    showData()
}

function loadData(imeXmla)
{
    let xhr = new XMLHttpRequest()
    
    xhr.onload = function(){
        if (this.status != 200) return

        let xmlDoc = this.responseXML

        let dishes = xmlDoc.getElementsByTagName('dish')

        let brojac = 0
        for(let dish of dishes)
        {
            brojac++
            if (brojac==10) break
            images.push('images/' + dish.getElementsByTagName('img')[0].textContent)

            let imgEl = document.createElement('img')
            imgEl.src = 'images/' + dish.getElementsByTagName('img')[0].textContent
            imgEl.className = "gallery-image"
            
            gallery.appendChild(imgEl)
        }
       
    }

    xhr.open('GET', imeXmla , true)
    xhr.send()
}



let number=0;

let galleryImages  = document.getElementsByClassName('gallery-image')
let currentImageIndex = 0

function showData()
{
    
    setInterval(changeImage, 1000);
    
   //setTimeout(automatic, 3000);  // every 3 seconds
}

/*
function automatic(){

    slika.style.opacity = 0
   
    number = (number+1)% images.length

    slika.src=images[number]
    slika.style.opacity = 1

    setTimeout(automatic,3000);
}
*/



function changeImage() {

  gallery.style = "border: 5px double white;"
  galleryImages[currentImageIndex].style.opacity = 0;
  
  currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
  
  galleryImages[currentImageIndex].style.opacity = 1;

  //setInterval(changeImage, 1000);
}

