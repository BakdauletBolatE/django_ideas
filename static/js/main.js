const swiper = new Swiper('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    },
    
  });

  function getName (str){
    if (str.lastIndexOf('\\')){
        var i = str.lastIndexOf('\\')+1;
    }
    else{
        var i = str.lastIndexOf('/')+1;
    }						
    var filename = str.slice(i);			
    var uploaded = document.getElementById("fileformlabel");
    uploaded.innerHTML = filename;
}


const ratings = document.querySelectorAll('.rate');

if (ratings){
  initRatings()
}

function initRatings(){
  let ratingActive,ratingValue;
  ratings.forEach(rating=>{
    initRating(rating);
  });

  function initRating(rating){
    initRatingVars(rating);
    setRatingActiveWidth();

    if (rating.classList.contains('rating__set')){
      setRating(rating);
    }
  }

  function initRatingVars(rating){
    ratingActive = rating.querySelector('.rate__active');
    ratingValue = rating.querySelector('.rate__value');
  }

  function setRatingActiveWidth(index = ratingValue.innerHTML){
    const ratingActiveWidth = index / 0.05;
    ratingActive.style.width = `${ratingActiveWidth}%`;

  }

  function setRating(rating){
    const ratingItems = rating.querySelectorAll('.rate__item');
    ratingItems.forEach((item,i)=>{
      item.addEventListener('click',()=>{
        initRating(rating);
        ratingValue.innerHTML = i+1;
        setRatingActiveWidth();
        
      })
    })
  }
}