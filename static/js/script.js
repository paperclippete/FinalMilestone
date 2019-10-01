$(document).ready(() => {
    getTheme(); 
    

    // Solid Navbar colour on toggler click
    $(".navbar-toggler").on('click', () => {
        if ($('.navbar').css("background-color") === '--dark-color') {
            return $('.navbar').css({"background-color": '--dark-color'});
        } else {
            $('.navbar').css({"background-color": '--dark-color'});
            $('.navbar').removeClass('navbar-effect');
        }
    });
    
    // Solid Navbar on scroll
    $(window).scroll(() => {
        if($(this).scrollTop() > 30) {
            $('.navbar').css({"background-color": '--dark-color'});
            $('.navbar').removeClass('navbar-effect');
        }
        else {
            $('.navbar').addClass('navbar-effect');
        }
    });
    
    // FAB Button for setting site theme
    $('#zoomBtn').click(() => {
        $('.zoom-menu').toggleClass('hidden')
        $('.zoom-btn-sm').toggleClass('scale-out');
    });
    
    $('.zoom-btn-sm').click(function() {
        const btn = $(this);
        
        if (btn.hasClass('zoom-btn-tangerine')) {
            localStorage.setItem('theme', 'tangerine');
            
        }
        else if (btn.hasClass('zoom-btn-grass')) {
            localStorage.setItem('theme', 'grass');
            
        }
        else if (btn.hasClass('zoom-btn-raspberry')) {
            localStorage.setItem('theme', 'raspberry');
            
        }
        else if (btn.hasClass('zoom-btn-sunshine')) {
            localStorage.setItem('theme', 'sunshine');
           
        }
        else {
            localStorage.setItem('theme', 'blueberry');
            
        }
    
    getTheme();    
        
    });
    
    function setTheme(theme) {
        $(':root').css('--main-color', `var(--${theme})`);
        $(':root').css('--dark-color', `var(--${theme}nav)`);
        $(':root').css('--main-background', `var(--${theme}back)`);
    
    }
    
    function getTheme() {
        if (localStorage.getItem('theme')) {
            setTheme(localStorage.getItem('theme'));
        } else {
            setTheme('sunshine');
        }
    }
    
    getTheme();
    
    //nav-link bounce effect
    $('.navbar-brand').mouseenter(function() {
        $(this).addClass("animated tada")
    }); 
    
    $('.navbar-brand').mouseleave(function() {
        $(this).removeClass("animated tada")
    });
    
    $('.nav-item').mouseenter(function() {
        $("a", this).addClass("animated tada")
    }); 
    
    $('.nav-item').mouseleave(function() {
        $("a", this).removeClass("animated tada")
    });
    
});

// Horizontal Slider by https://codepen.io/toddwebdev
function scrollSection() {
    let slider = this;
    let isDown = false;
    let startX;
    let scrollLeft;
    
    slider.addEventListener('mousedown', (elem) => {
        isDown = true;
        slider.classList.add('active');
        startX = elem.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });
    
    slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.classList.remove('active');
    });
        
    slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.classList.remove('active');
    });
        
    slider.addEventListener('mousemove', (elem) => {
        if (!isDown) return;
        elem.preventDefault();
        const x = elem.pageX - slider.offsetLeft;
        const walk = (x - startX) * 3; //scroll-fast
        slider.scrollLeft = scrollLeft - walk;
        
     });
}
    


function modalMemForm(event)  {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const membership_level = button.data('level'); // Extract info from data-* attributes

    // Update modal with required membership forms
    const modal = $(this)
    modal.find('.modal-title').html(`You've chosen to be a<span class="${membership_level}-text"><strong> ${membership_level.toUpperCase()}</strong></span> member!`);

    if (membership_level === 'bronze') {
        modal.find('#payment-form').css('display', 'none');
        modal.find('#bronze-form').css('display', 'block');
    }
    else if (membership_level === 'silver') {
        modal.find('#payment-form').css('display', 'block');
        modal.find('#bronze-form').css('display', 'none');
        modal.find('form').attr('action', "{% url 'membership' 'silver' %}");
    }
    else {
        modal.find('#payment-form').css('display', 'block');
        modal.find('#bronze-form').css('display', 'none');
        modal.find('form').attr('action', "{% url 'membership' 'gold' %}");
    }
}