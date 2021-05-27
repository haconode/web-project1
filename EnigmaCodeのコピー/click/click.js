function copyToClipboard(){
    //コピー対象を変数定義
    var copyTarget = document.getElementById("code");

    //コピー対象のテキスト選択
    copyTarget.select();

    //選択テキストのコピー
    document.execCommand("Copy");

    //コピーを知らせる
    // alert("コピー完了:" + copyTarget.value);
}

function cutToClipboard() {
    //コピー対象を変数定義
    var copyTarget = document.getElementById("answer");

    //コピー対象のテキスト選択
    copyTarget.select();
 
    //選択テキストのコピー
    document.execCommand("Copy");
 
    //コピーを知らせる
    // alert("コピー完了:" + copyTarget.value);
}