



  function viewimage2(imgg,cnty) {
    scounter = cnty-1;
    document.getElementById(img9.id).src = document.getElementById(imgg.id).src;
  }


  let scounter = 0;
  function slidemyimage(numy) {
     ct=5;
      let sidephotos = ["img1","img2","img3","img4","img5","img6","img7","img8","img9"]
      if (numy == 1) 
      {
          if(scounter >= ct-1){ 	scounter = 0;
          }  else{scounter++;}
          document.getElementById(img9.id).src = document.getElementById(sidephotos[scounter]).src;
      }
      if (numy == 2) 
      {
  
          if(scounter == 0){
              scounter = ct-1;
          }
          else{
              scounter--;
          }
          document.getElementById(img9.id).src = document.getElementById(sidephotos[scounter]).src;
      }
  }
  
   function viewspan1() {
      document.getElementById(sp1.id).style.opacity = 1;
      document.getElementById(sp2.id).style.opacity = 1;
   }
  
   function viewspan2() {
      document.getElementById(sp1.id).style.opacity = 0;
      document.getElementById(sp2.id).style.opacity = 0;
   }
  
  

   function setcolor2(subfld,mainfold,nimg) {
    let xx1= ["img1","img2","img3","img4","img5","img6","img7","img9","img9"];
    let xx2= ["01","02","03","04","05","06","07","08","09"];
    let numimg = nimg;
    let mainfld = mainfold;
    document.getElementById(img9.id).src = "/static/clothshop/img/"+mainfld+"/"+subfld+"/subimage-01.webp";
    for (let i = 0; i < numimg; i++) {                            
        document.getElementById(xx1[i]).src = "/static/clothshop/img/"+mainfld+"/"+subfld+"/subimage-"+xx2[i]+".webp"; }
    }

            
    function addtocart() {
        
        let mystock = parseInt(document.getElementById(lblCartCount.id).innerHTML);
        mystock = mystock + 1;
        document.getElementById(lblCartCount.id).innerHTML = mystock; 
        console.log(mystock);
    }

    function removefromcart() {
        
        let mystock = parseInt(document.getElementById(lblCartCount.id).innerHTML);
        mystock = mystock - 1;
        if (mystock <=0 ) {mystock=0;}
        document.getElementById(lblCartCount.id).innerHTML = mystock; 
        console.log(mystock);
    }