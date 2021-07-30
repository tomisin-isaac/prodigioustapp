var loginForm = document.getElementById("loginForm");
        var RegForm = document.getElementById("RegForm");
        var Indicator = document.getElementById("Indicator");

        function register(){
            RegForm.style.transform = "translateX(0px)";
            loginForm.style.transform = "translateX(0px)";
            Indicator.style.transform =  "translateX(100px)";
        }

        function login(){
            RegForm.style.transform =  "translateX(300px)";
            loginForm.style.transform =  "translateX(300px)";
            Indicator.style.transform =  "translateX(0px)";
        }