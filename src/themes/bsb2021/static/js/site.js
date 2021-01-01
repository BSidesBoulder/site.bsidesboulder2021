$(document).ready(onReady());

function onReady() {
    $('#showExplanationHref').click(showExplanationDialog);
}

function init() {

}

function showExplanationDialog() {
    console.log('showExplanationDialog')
    $('#show-explanation-dialog').dialog({
        height: 300,
        width: 500,
        position: { my: "center", at: "center", of: window }
    });
}