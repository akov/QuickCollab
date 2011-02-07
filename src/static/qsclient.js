//qsclient.js 
//javascript component of Quickshare that alerts
//the server of changes 

var prev_text;
var dmp = new diff_match_patch();
delay_interval = 5000
$(document).ready(function() {
   prev_text = $("#text_area").val();
   var editor = CodeMirror.fromTextArea("text_area", {
		  parserfile: ["tokenizejavascript.js", "parsejavascript.js"],
		  path: "static/codemirror/js/",
		  stylesheet: "static/codemirror/css/jscolors.css",
        width: "650px",
        height: "dynamic",
        tabmode: "spaces",
		});
  setTimeout("changesPushLoop()", delay_interval);
});

function changesPushLoop()
{
  $("#push_button").click(function(){
      $.ajax({
         type: "POST",
         data: {save: false,
                text_patch : dmp.patch_toText(dmp.patch_make(prev_text, editor.getCode()))},
         success: function(data){
               prev_text = data;
               editor.setCode(data);
            }
         })
      return false;
   })
   setTimeout("changesPushLoop()", delay_interval);
}
