function toggle_form_widget(commentTogglerId, formWidgetId) {
    var formWidget = document.getElementById(formWidgetId);
    if (formWidget.style.display === "none") {
        formWidget.style.display = "block";
    } else {
        formWidget.style.display = "none";
    }
}