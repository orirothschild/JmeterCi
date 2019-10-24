import groovy.json.JsonSlurper;
import org.apache.jmeter.assertions.AssertionResult;
import groovy.util.logging.Log;
class DBChecker{
	String failureMessage = '';

	public void DBContainsRequiredFields(ArrayList results,List variantNames,String msg){
	String resultmsg;
	results.each{resultArray -> 
			variantNames.each{var ->
				if(!(resultArray.keySet().contains(var))){
					failureMessage+=" - ${var} - "
				}

			}
		}
		if(failureMessage?.trim()){
			failureMessage = msg + failureMessage;
		}
			
	}
	//*****************************************DB methods**********************************************
	
	public void databaseNotEqualsStrings(String oldValue,String newValue, String msg){
		if(msg == null || oldValue == null || newValue == null){
		 	this.failureMessage += " databaseNotEquals got null values\n";
		 	return;
		 }
		if(oldValue.equals(newValue)){
			this.failureMessage += msg + "\n\n";
		}
	}

	public void databaseEqualsStrings(String oldValue,String newValue, String msg){
		if(msg == null || oldValue == null || newValue == null){
		 	this.failureMessage += " databaseEquals got null values\n";
		 	return;
		 }
		if(!oldValue.equals(newValue)){
			this.failureMessage += msg + "\n\n";
		}
	}

	public void databaseEquals(long oldValue,long newValue, String msg){
		if(msg == null || oldValue == null || newValue == null){
		 	this.failureMessage += " databaseNotEquals got null values\n";
		 	return;
		 }
		if(!oldValue==newValue){
		 groovy.util.logging.Log.info(hello);
			this.failureMessage += msg + "\n\n";
		}
	}

	public void databaseNotEquals(long oldValue,long newValue, String msg){
		if(msg == null || oldValue == null || newValue == null){
		 	this.failureMessage += " databaseNotEquals got null values\n";
		 	return;
		 }
		if(oldValue==newValue){
			this.failureMessage += msg + "\n\n";
		}
	}

public void databaseEquals(long oldValue,String newValue, String msg){
		if(msg == null || oldValue == null || newValue == null){
		 	this.failureMessage += " databaseNotEquals got null values\n";
	 		return;
		 }
		if(!oldValue==newValue){
			this.failureMessage += msg + "\n\n";
		}
	}

	
	public void databaseEqualsWithResultArray(String oldValue,String newValue, String msg){
		if(msg == null || oldValue == null || newValue == null){
		 	this.failureMessage += " databaseNotEquals got null values\n";
		 	return;
		 }
		if(!oldValue.equals(newValue)){
			this.failureMessage += msg + "\n\n";
		}
	}

	public String getFailureMassage(){
		return this.failureMessage;
	}

	}

	DBChecker Checker = new DBChecker();
	vars.putObject('DBChecker',Checker);
	props.put('DBChecker',Checker);
