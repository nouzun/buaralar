$(document).ready(function(){
    language_complete = navigator.language.split("-");
    language = (language_complete[0]);
    console.log("Sprache (root): %s", language);
    language = "tr";
    i18n.init({ lng: language, debug: true, resGetPath: "/static/locales/__lng__/__ns__.json"}, function() {
        // save to use translation function as resources are fetched
        var title = i18n.t("site_name") + " | " + i18n.t("site_description");
        document.title = title;
        $(".container").i18n();
    });
});