$(document).ready(function() {
    
    // Random Background 
    // Gradient Design from https://www.gradientmagic.com
    const blueberry = "linear-gradient(45deg, rgb(126, 0, 208) 0%, rgb(126, 0, 208) 33%, rgb(105, 0, 173) 33%, rgb(105, 0, 173) 34%, rgb(84, 0, 138) 34%, rgb(84, 0, 138) 42%, rgb(59, 0, 97) 42%, rgb(59, 0, 97) 56%, rgb(50, 0, 82) 56%, rgb(50, 0, 82) 67%, rgb(45, 0, 74) 67%, rgb(45, 0, 74) 99%, rgb(28, 0, 45) 99%, rgb(28, 0, 45) 100%)";
    const raspberry = "linear-gradient(45deg, rgb(231, 0, 38) 0%, rgb(231, 0, 38) 33%, rgb(218, 0, 36) 33%, rgb(218, 0, 36) 34%, rgb(206, 0, 34) 34%, rgb(206, 0, 34) 42%, rgb(195, 0, 32) 42%, rgb(195, 0, 32) 56%, rgb(177, 0, 30) 56%, rgb(177, 0, 30) 67%, rgb(167, 0, 27) 67%, rgb(167, 0, 27) 99%, rgb(140, 0, 23) 99%, rgb(140, 0, 23) 100%)";
    const sunshine = "linear-gradient(45deg, rgb(255, 195, 0) 0%, rgb(255, 195, 0) 33%, rgb(232, 178, 0) 33%, rgb(232, 178, 0) 34%, rgb(222, 170, 0) 34%, rgb(222, 170, 0) 42%, rgb(204, 156, 0) 42%, rgb(204, 156, 0) 56%, rgb(189, 145, 0) 56%, rgb(189, 145, 0) 67%, rgb(171, 131, 0) 67%, rgb(171, 131, 0) 99%, rgb(138, 106, 0) 99%, rgb(138, 106, 0) 100%)";
    const grass = "linear-gradient(45deg, rgb(0, 205, 65) 0%, rgb(0, 205, 65) 33%, rgb(0, 190, 60) 33%, rgb(0, 190, 60) 34%, rgb(0, 173, 55) 34%, rgb(0, 173, 55) 42%, rgb(0, 148, 47) 42%, rgb(0, 148, 47) 56%, rgb(0, 121, 39) 56%, rgb(0, 121, 39) 67%, rgb(0, 101, 32) 67%, rgb(0, 101, 32) 99%, rgb(0, 70, 22) 99%, rgb(0, 70, 22) 100%)";
    const tangerine = "linear-gradient(45deg, rgb(242, 98, 4) 0%, rgb(242, 98, 4) 33%, rgb(222, 88, 4) 33%, rgb(222, 88, 4) 34%, rgb(210, 84, 4) 34%, rgb(210, 84, 4) 42%, rgb(193, 78, 4) 42%, rgb(193, 78, 4) 56%, rgb(181, 73, 4) 56%, rgb(181, 73, 4) 67%, rgb(167, 67, 4) 67%, rgb(167, 67, 4) 99%, rgb(140, 57, 4) 99%, rgb(140, 57, 4) 100%)";
    
    const bg = [blueberry, raspberry, tangerine, grass, sunshine];
    let random = Math.floor(Math.random() * bg.length);
        
    $("#site-background").css({"background-image": bg[random]});
    
    // Matching body color 
    const blueberryback = "#2d004a";
    const raspberryback = "#a7001b";
    const sunshineback = "#ab8300";
    const grassback = "#006520";
    const tangerineback = "#b54904";
    
    if ($("#site-background").css('background-image') === blueberry) {
        $('body').css({"background-color": blueberryback});
    }
    if ($("#site-background").css('background-image') === raspberry) {
        $('body').css({"background-color": raspberryback});
    }
    if ($("#site-background").css('background-image') === sunshine) {
        $('body').css({"background-color": sunshineback});
    }
    if ($("#site-background").css('background-image') === grass) {
        $('body').css({"background-color": grassback});
    }
    if ($("#site-background").css('background-image') === tangerine) {
        $('body').css({"background-color": tangerineback});
    }
    
    // Solid Navbar colour on toggler click
    $(".navbar-toggler").on('click', function(){
        let colour = $('body').css("background-color");
        if ($('.navbar').css("background-color") === colour) {
            return $('.navbar').css({"background-color": colour});
        } else {
            $('.navbar').css({"background-color": colour});
            $('.navbar').toggleClass('navbar-effect');
        }
    })
    
    // Solid Navbar on scroll
    $(window).scroll(function() {
        let colour = $('body').css("background-color");
        if($(this).scrollTop() > 30) {
            $('.navbar').css({"background-color": colour});
            $('.navbar').removeClass('navbar-effect');
        }
        else {
            $('.navbar').addClass('navbar-effect');
        }
    })
    
    
    
   

    
});