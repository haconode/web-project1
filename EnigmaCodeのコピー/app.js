function Encrypt(){
    //テキスト読み込み
    const textbox = document.getElementById("message").value;

    //暗号化されたテキスト出力
    document.getElementById("answer").value = textbox;

    //エニグマコード出力
    const code = "444";
    document.getElementById("code").value = code;
}

function Decrypt(){
    //テキスト読み込み
    const textbox = document.getElementById("message").value;

    //エニグマコード読み込み
    const code = document.getElementById("code").value;

    //復号化されたテキスト出力
    document.getElementById("answer").value = textbox;
}
