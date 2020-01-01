package il.co.selenium.ls;

import com.thoughtworks.selenium.Selenium;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.WebDriver;
import com.thoughtworks.selenium.webdriven.WebDriverBackedSelenium;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.regex.Pattern;
//import static org.apache.commons.lang3.StringUtils.join;

public class job {
	private Selenium selenium;

	@Before
	public void setUp() throws Exception {
		WebDriver driver = new FirefoxDriver();
		String baseUrl = "https://www.katalon.com/";
		selenium = new WebDriverBackedSelenium(driver, baseUrl);
	}

	@Test
	public void testUntitledTestCase() throws Exception {
		selenium.open("https://www.nofshonit.co.il/");
		selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='׳�?׳×׳—׳‘׳¨׳•׳× / ׳�?׳¨׳©׳�׳�?'])[1]/following::button[1]");
		selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='׳�?׳�׳©׳� ׳¢׳� ׳’׳•׳’׳�'])[1]/following::button[1]");
		selenium.click("xpath=(//input[@name='email'])[2]");
		selenium.type("xpath=(//input[@name='email'])[2]", "shabtaiuser_935352034@dts-4u.com");
		selenium.type("name=password", "Hello_0363");
		selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='׳�?׳×׳—׳‘׳¨׳•׳× ׳‘׳�׳�׳¦׳¢׳•׳× ׳�׳™׳™׳�'])[1]/following::button[1]");
		selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='׳�?׳×׳—׳‘׳¨׳•׳× ׳‘׳•׳¦׳¢׳�? ׳‘׳�?׳¦׳�׳—׳�?'])[1]/following::button[1]");
		selenium.click("//div[@id='__next']/div/div[2]/div[2]/div/div/div/div/div/div[3]/i");
		selenium.click("link=׳�?׳×׳ ׳×׳§");
	}

	@After
	public void tearDown() throws Exception {
		selenium.stop();
	}
}
