function doGet(request) {
SpreadsheetApp.getActiveSpreadsheet().getActiveSheet().appendRow([request.parameter.author, request.parameter.message, new Date()]); 

var template = HtmlService.createTemplateFromFile('Blog');

return template.evaluate();
}

function getMessages() {
var ms = SpreadsheetApp.getActiveSheet();

var data = ms.getRange(2, 1, ms.getLastRow()-1, 3).getValues();

return JSON.stringify(data);
}