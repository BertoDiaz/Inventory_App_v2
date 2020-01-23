/**
 * Shows7hide a lab images
 * @param {id} id
 */
 var modal;

function open_modal(url, title)
{
    modal = $('#popup').dialog(
    {
        title: title,
        modal: true,
        width: 500,
        resizable: false
    }).dialog('open').load(url)
}

function close_modal()
{
    modal.dialog("close");
}
