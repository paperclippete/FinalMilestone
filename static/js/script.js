$(document).ready(function() {
    getTheme();
    

    // Solid Navbar colour on toggler click
    $(".navbar-toggler").on('click', function(){
        if ($('.navbar').css("background-color") === '--dark-color') {
            return $('.navbar').css({"background-color": '--dark-color'});
        } else {
            $('.navbar').css({"background-color": '--dark-color'});
            $('.navbar').toggleClass('navbar-effect');
        }
    });
    
    // Solid Navbar on scroll
    $(window).scroll(function() {
        if($(this).scrollTop() > 30) {
            $('.navbar').css({"background-color": '--dark-color'});
            $('.navbar').removeClass('navbar-effect');
        }
        else {
            $('.navbar').addClass('navbar-effect');
        }
    });
    
    // FAB Button for setting site theme
    $('#zoomBtn').click(function() {
        $('.zoom-menu').toggleClass('hidden')
        $('.zoom-btn-sm').toggleClass('scale-out');
        
        
    });
    
    $('.zoom-btn-sm').click(function() {
        var btn = $(this);
        
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
        console.log(theme);
        $(':root').css('--main-color', 'var(--'+theme+')');
        $(':root').css('--dark-color', 'var(--'+theme+'nav)');
        $(':root').css('--main-background', 'var(--'+theme+'back)');
    
    }
    
    function getTheme() {
        if (localStorage.getItem('theme')) {
            setTheme(localStorage.getItem('theme'));
        } else {
            setTheme('sunshine');
        }
    }
    
    //nav-link bounce effect
    $('.navbar-brand').mouseenter(function() {
        $(this).addClass("animated tada")
    }) 
    
    $('.nav-item').mouseleave(function() {
        $("a", this).removeClass("animated tada")
    })
    
    $('.nav-item').mouseenter(function() {
        $("a", this).addClass("animated tada")
    }) 
    
    $('.nav-item').mouseleave(function() {
        $("a", this).removeClass("animated tada")
    })
    

    
   

    
});