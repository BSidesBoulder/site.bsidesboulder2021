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
    load_mailbox();
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

function read_email(e,data) {
    var email_id = $(this).attr('id');
    var datafield = $('#datafeed').val();
    
    // Deselect other email messages and toggle email
    $(".selected").removeClass('selected');
    $(this).toggleClass('selected');

    $.get(datafield, function(data){
        var i;
        for (i = 0; i< data.mailbox.length; i++){
            msg = atob(data.mailbox[i].message);
            if (email_id == data.mailbox[i].id) {
                // load the attachment
                var attachment = "";
                if (data.mailbox[i].attachment) {
                    console.log('Has Attachment')
                    attachment = `<div class="attachment">
                        <div class="file"><a href="/attachments/${data.mailbox[i].attachment}" target="_blank"><i class="far fa-file-pdf"></i> ${data.mailbox[i].attachment}</a></div>
                    </div>
                    `
                }

                var message = `
                <div class="mailheader">
                    <div class="subject">${data.mailbox[i].subject}</div>
                    <hr class="mailsubject">
                    <div class="fromfield">${data.mailbox[i].fromfieldFriendly} &lt;${data.mailbox[i].fromfield}&gt;</div>
                    <div class="datefield"><span class="bolder small-spacer">Sent:</span>${data.mailbox[i].longdate}</div>
                    <hr class="mailmessage" />
                    <div class="message">${msg}</div>
                    ${attachment}
                </div>`;
                $('.mail').html(message);
            }
        }

        // If the email is currently "unread", wait for two seconds before
        // marking it "read".
        if (!getEmailRead(email_id)) {
            setTimeout(function() {
                setEmailRead(email_id);
            }, 2000);
        }
    })
}

function load_mailbox() {
    var datafield = $('#datafeed').val();
    var id;
    if (datafield)
    {
        $.get(datafield,function(data) {
            var i;
            var container = document.getElementById('maillist_container');
            var email_icon;
            for (i = 0; i < data.mailbox.length;i++) {
                if (i !== 0) {
                    var mailhr = document.createElement('hr');
                    mailhr.setAttribute('class','maildivider');
                    container.appendChild(mailhr);

                }
                // lets create the object
                var maillist_row = document.createElement('div');
                if (id === void(0)) {
                    id = data.mailbox[i].id;
                }
                var readStatus = getEmailRead(data.mailbox[i].id);
                if (readStatus) {
                    email_icon = "fa-envelope-open-text";
                } else {
                    email_icon = "fa-envelope";
                }


                maillist_row.setAttribute('id', data.mailbox[i].id);
                maillist_row.setAttribute('class', 'maillist_row');
                maillist_row.innerHTML = `
                    <div class="row">
                        <div class="tr">
                            <div class="maillist_row_image">
                                <i class="fas fa-envelope" id="email-icon-${data.mailbox[i].id}-unread"></i>
                                <i class="fas fa-envelope-open-text" id="email-icon-${data.mailbox[i].id}-read"></i>
                            </div>
                            <div class="maillist_row_sender">${data.mailbox[i].fromfieldFriendly}</div>
                            <div class="maillist_row_date">${data.mailbox[i].shortdate}</div>
                        </div>
                    </div>    
                    <div class="row">
                        <div class="tr">
                            
                            <div class="maillist_row_subject">${data.mailbox[i].subject}</div> 
                        </div   
                    </div>
                    `;
                container.appendChild(maillist_row);

                if (!readStatus)
                {
                    $(`#email-icon-${data.mailbox[i].id}-read`).hide();
                }
                else {
                    $(`#email-icon-${data.mailbox[i].id}-unread`).hide();
                }
            }

            $('.maillist_row').click(read_email);
            $(`#${id}`).trigger("click");
        });
    }

}

function setEmailRead(id) {
    $(`#email-icon-${id}-read`).show();
    $(`#email-icon-${id}-unread`).hide();
    localStorage.setItem(id,'read');
}

function getEmailRead(id) {
    var value = localStorage.getItem(id);
    if (value ==='read') {
        return true;
    }
    else {
        return false;
    }
}

function showMnuFile() {
    document.getElementById("mnuFileDropdown").classList.toggle("show");
}

function showMnuDelete() {
    document.getElementById("mnuDeleteDropdown").classList.toggle("show");
}

  // Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

  function DeleteUi() {
      $("#user-interface").remove();
  }

  function markEmailAsUnread() {
      var email_id = $('.selected').attr('id');
      localStorage.setItem(email_id,'');
      $(`#email-icon-${email_id}-read`).hide();
      $(`#email-icon-${email_id}-unread`).show();
  }
