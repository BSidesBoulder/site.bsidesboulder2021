$(document).ready(onReady());

function onReady() {
    init();

    // Login Page Initializers
    $('#showExplanationHref').click(showExplanationDialog);
    $('#btnSignIn').click(clickSignIn);
    $('#mailbox-folders-tree').jstree({
        core: {
            themes: {dots: false}
        }
    });
    $('#mailbox-folders-tree').on('changed.jstree', jstreeChanged);

    // Mailbox Page Initializers
    $('#btnSignOut').click(clickSignOut);
    console.log('OnReady Complete...');
}

function init() {
    // if you have already seen the login page you can skip it.
    if (Cookies.get('loggedin') && location.pathname === '/'){
        location.href = "/mailbox/";
    }
}

function showExplanationDialog() {
    console.log('showExplanationDialog')
    $('#show-explanation-dialog').dialog({
        height: 300,
        width: 500,
        position: { my: "center", at: "center", of: window }
    });
}

function clickSignIn() {
    Cookies.set('loggedin', true);
    location.href = '/mailbox/';
}

function clickSignOut() {
    console.log('Signout');
    Cookies.set('loggedin', '');
    location.href = '/';
}

function jstreeChanged(e,data) {
    console.log(data.selected);
}