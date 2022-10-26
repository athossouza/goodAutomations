// Add an element with organization name of user logged
// Para adicionar mais campo, é só copiar a função inteira e renomear specialCustomField1 para 2, 3 e etc.
//Copiar daqui
specialCustomField1()
function specialCustomField1() {

  nomeDaEmpresa = "CISER ARAQUARI" // Nome da organização exatamente como está no Zendesk
  idCampo = "10376447625236" // ID do campo de ticket

	orgNameFromUserLogged = HelpCenter.user.organizations[0].name;
	orgNameFromSettings = nomeDaEmpresa;

	var custoFieldID = idCampo;
	var hiddenField = "request_custom_fields_" + custoFieldID


	if (orgNameFromUserLogged != orgNameFromSettings) {
  	document.getElementsByClassName(hiddenField)[0].setAttribute("hidden", true);
	};
};
//Até aqui
