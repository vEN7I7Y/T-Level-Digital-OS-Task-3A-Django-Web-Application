//function to increase the font size
jQuery(function () {
    const font_Size = $("body").css("font-size");
    document.getElementById("text-increase").addEventListener("click", () => {
        let current_Size = parseInt(font_Size);
        let new_Size = `${current_Size + 10}px`
        $("body").css("font-size")
        $("body").css("font-size", new_Size)
    })

    //function to decrease the font
    document.getElementById("text-decrease").addEventListener("click", () => {
        let current_Size = parseInt(font_Size);
        let new_Size = `${current_Size - 1}px`
        $("body").css("font-size")
        $("body").css("font-size", new_Size)
    })
    //function to reset the font siz
    document.getElementById("reset").addEventListener("click", () => {
        $("body").css("font-size")
        $("body").css("font-size", font_Size)
    })


    //darkmode toggle switch 
    document.getElementById("darkmode-switch").addEventListener("click", () => {
        const background_Color = $("body").css("background-color");
        const dark = "rgb(1, 1, 0)";
        const light = "rgb(232, 242, 218)";
        if (background_Color === dark) {
            $("body").css("background-color", light);
        }
        else {
            $("body").css("background-color", dark);
        }
    });
})