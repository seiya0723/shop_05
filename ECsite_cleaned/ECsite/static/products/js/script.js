//ページが読み込みされた時に function(){} の中の処理を実行する。
window.addEventListener("load" , function (){
    //$から始まるものはjQuery構文、予めjQueryをインストールしておかないと使えない
    //class名add_imageに対して、クリックした時、idがimage_areaの中にinputタグを追加する
    //$(".add_image").on("click",function(){ $("#image_area").append('<input type="file" name="image">'); });

    //$(".input_image").on("input",function(){ $("#image_area").append('<input class="imput_image" type="file" name="image">'); })
    $(document).on("input", ".input_image" ,function(){ $("#image_area").append('<input class="input_image" type="file" name="image">'); })
});

