
let podaciDiv = document.getElementById("podaci")

let dinners = []

function loadData(imeXmla)
{
    let xhr = new XMLHttpRequest()
    
    xhr.onload = function(){
        if (this.status != 200) return

        let xmlDoc = this.responseXML

        let dishes = xmlDoc.getElementsByTagName('dish')

        for(let dish of dishes)
        {
            let obj = {}

            obj['name'] = dish.getElementsByTagName('name')[0].textContent
            obj['cost'] = Number(dish.getElementsByTagName('cost')[0].textContent)
            obj['description'] = dish.getElementsByTagName('description')[0].textContent
            obj['img'] = 'images/' + dish.getElementsByTagName('img')[0].textContent
            
            let sastojci = dish.getElementsByTagName('ingredients')[0].getElementsByTagName('ingredient')
            let ingredients = []

            
            for(let sastojak of sastojci)
            {
                ingredients.push(sastojak.textContent)
            }
            
            obj['ingredients'] = ingredients
            obj['liked'] = false

            dinners.push(obj)  
        }

        showData()
        azurirajTabelu()
    }

    xhr.open('GET', imeXmla, true)
    xhr.send()
}

let searchName = document.getElementById('inp-name')
let cena = document.getElementById('inp-cena')
let manje = document.getElementById('rb-cena-manja')
let vece = document.getElementById('rb-cena-veca')
let sastojak = document.getElementById('sel-ingredient')

function checkFilters(dish)
{
    if (dish['name'].includes(searchName.value) && 
        ((manje.checked && (dish['cost']<=Number(cena.value)) || cena.value=='') ||
        (vece.checked && dish['cost']>=Number(cena.value)) ) )
        //&& dish['ingredients'].includes(sastojak.value)) 
        return true
    return false
}

let recept  = document.getElementById('recept')
let naslovRecept = document.getElementById('naslovRecept')

function clearFilters(){
    searchName.value = '';
    cena.value = '';
    manje.checked = false;
    vece.checked = true;
    recept.innerHTML = ''
    naslovRecept.hidden = true
    showData()
}

function showData(){

    let tabela = document.createElement('table')
    console.log(tabela)

    for(let dish of dinners)
    {

        if (!checkFilters(dish)) continue

        let row = document.createElement('tr')

        row.onclick = function(){
            console.log('Click')
            
            recept.innerHTML = `<p>${dish['description']}</p>`
            naslovRecept.hidden = false
        }

        let rowIme  = document.createElement('tr')
        
        let img = document.createElement('img')
        img.src = dish['img']

        img.on
        
        let ulLista = document.createElement('ul')
        
        for (let ingredint of dish['ingredients'])
        {
            let li = document.createElement('li')
            li.innerHTML = ingredint

            ulLista.appendChild(li)
        }


        let td1 = document.createElement('td')
        let td2 = document.createElement('td')
        let td3 = document.createElement('td')
        let td4 = document.createElement('td')
        let td5 = document.createElement('td')

        td1.appendChild(img)
        td1.id="slika"
        td2.innerHTML = `<h2>${dish['name']}</h2>`
        td3.innerHTML = `<p>Sastojci :</p>`
        td3.appendChild(ulLista)
        td4.innerHTML  = "$" + dish['cost']
        
        /*
        td5.innerHTML = `
        <input id="heart" type="checkbox" />
        <label for="heart">❤</label>`
        */
       
        let a = document.createElement('a')
        let imgSrce = document.createElement('img')
        imgSrce.src = "images/heart.png"
        if (dish['liked']) imgSrce.src="images/fullHeart.png"


        a.onclick = function(){
            dish['liked'] = !dish['liked']
            
            showData()
            azurirajTabelu()
        }
        
        
        a.appendChild(imgSrce)
        td5.id = "srce"
        td5.appendChild(a)

        td2.colSpan = 3;
        td2.style = "width: 250px;"
        rowIme.appendChild(td2)

        row.appendChild(td1)
        row.appendChild(td3)
        row.appendChild(td4)
        row.appendChild(td5)

        tabela.appendChild(rowIme)
        tabela.appendChild(row)
    }
    podaciDiv.innerHTML = ''
    podaciDiv.appendChild(tabela)
}


let lajkovani = document.getElementById('tabelaLajkovanih')
let naslovLajkovanih  = document.getElementById('naslovLajkovanih')
let total = document.getElementById('total')

function azurirajTabelu(){
    lajkovani.innerHTML = ''
    naslovLajkovanih.innerHTML = ''

    let spanNaslov = document.createElement('p')
    spanNaslov.innerHTML = "Lajkovano : "
    spanNaslov.style="border-bottom: 2px dotted #937465"

    let btnCancel = document.createElement('button')
    btnCancel.innerHTML =
     `<img src="images/x.png" style="height:40px"></img></a>`
    btnCancel.onclick= function(){
        izbrisiSveIzListeLajkovanih()
    }


    let tabela = document.createElement('table')

    let brojac = 0
    let suma = 0

    for(let dish of dinners)
    {
        if (!dish['liked']) continue

        let row = document.createElement('tr')

        let td1 = document.createElement('td')
        let td2 = document.createElement('td')
     
        td1.innerHTML = dish['name']
        td2.innerHTML  = "$" + dish['cost']


        row.appendChild(td1)
        row.appendChild(td2)

        tabela.appendChild(row)

        brojac++
        suma += Number(dish['cost'])
    }

    naslovLajkovanih.appendChild(spanNaslov)

    if (brojac == 0 ) lajkovani.innerHTML = `<strong>NEMA LAJKOVANIH JELA</strong>`
   
    lajkovani.appendChild(tabela)

    suma = Math.round(suma*100)/100;
    total.innerHTML = "<br>Total : " + brojac + "</br>Ukupna cena za pripremu izabranih jela : $" + suma + "<br>"

    if (brojac)  
        total.appendChild(btnCancel)
}

function izbrisiSveIzListeLajkovanih(){
    console.log('odlajkujem sve')
    for(let dish of dinners)
    {
        dish['liked'] = false
    }
    recept.innerHTML = ''
    naslovRecept.hidden = true
    showData()
    azurirajTabelu()
}
