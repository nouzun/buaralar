$(document).ready(function(){
    if ($.cookie("language") != "tr" && $.cookie("language") != "en") {
        language_complete = navigator.language.split("-");
        language = (language_complete[0]);
        //console.log("Sprache (root): %s", language);
    } else {
        language = $.cookie("language");
    }
    initLanguage(language);

    $("ul#ul-dropdown-language li").click(function(){
        language = $(this).attr("language");
        $.removeCookie('language', { path: '/' });
        $.cookie("language", language, { path: '/' });
        initLanguage(language);
    });
});

function initLanguage(language) {
    i18n.init({ lng: language, debug: true, resGetPath: "/static/locales/__lng__/__ns__.json"}, function() {
        // save to use translation function as resources are fetched
        var title = i18n.t("site_name") + " | " + i18n.t("site_description");
        document.title = title;

        $("#a-dropdown-language").html($('ul#ul-dropdown-language li[language="'+language+'"] a').html() + '&nbsp;<span class="caret"></span>');
        $('ul#ul-dropdown-language li[language="'+language+'"]').siblings().show();
        $('ul#ul-dropdown-language li[language="'+language+'"]').hide();

        $(".container").i18n();
    });
}