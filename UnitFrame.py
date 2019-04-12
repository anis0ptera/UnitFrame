# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# This class defines the setup, teardown, and all test cases for the fandor site suite.
# Test cases are in the form of methods like "testaPage".
class UnitFrame(unittest.TestCase):

	skip = True
	extension = "/films/sita_sings_the_blues#"

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.fandor.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
		self.assertTrue(True)

	def tryElementXpath(self,tag,text,level):
		if level > 1:
			try:
				self.driver.find_element_by_xpath("(//" + tag + "[contains(text(),'" + text + "')])[" + level + "]")
			except NoSuchElementException:
				return False
			return True
		else:
			try:
				self.driver.find_element_by_xpath("(//" + tag + "[contains(text(),'" + text + "')])")
			except NoSuchElementException:
				return False
			return True

	@unittest.skipIf(skip,"Skipping...")
	def testaPage(self): # /
		#Verify that correct page is invoked by requesting URL
		self.driver.get(self.base_url + self.extension)
		#print(self.driver.title)
		assert "Sita Sings the Blues, the Animated film by Nina Paley | Fandor" in self.driver.title
		return

	@unittest.skipIf(skip,"Skipping...")
	def testbUtton(self):
		#Verify that clicking Learn More button brings up pop-up
		self.driver.get(self.base_url + self.extension)
		buttonLearn = self.driver.find_element_by_xpath("//div[2]/div/button")
		#buttonLearn = self.driver.find_element_by_class_name("small.tertiary.radius")
		#buttonLearn = self.driver.find_element_by_id('learn-more-modal')
		print(buttonLearn.text)
		assert "Learn More" in buttonLearn.text
		buttonLearn.click()
#		Xception = False
		try:
			self.driver.find_element_by_id('learn-more-modal')
			#self.driver.find_element_by_class_name("button small tertiary radius")
		except NoSuchElementException:
			self.assertTrue(False)
#			Xception = True
#		self.assertFalse(Xception)
		try:
			closeModal = self.driver.find_element_by_css_selector("#learn-more-modal > a.close-reveal-modal")
		except NoSuchElementException:
			self.assertTrue(False)
		closeModal.click()
		return

	@unittest.skipIf(skip,"Skipping...")
	def testcNewrel(self): # /
		#Verify that selecting Films: New Releases from dropdown goes to New Releases page
		self.driver.get(self.base_url + self.extension)
		try:
			filmsLink = self.driver.find_element_by_class_name("films-link")
		except NoSuchElementException:
			self.assertTrue(False)
		filmsLink.click()
		#newReleases = self.driver.find_element_by_xpath("(//a[contains(text(),'New Releases')])[2]")
		newReleases = self.driver.find_element_by_xpath("(//a[contains(text(),'New Arrivals')])[2]")
		#assert "New Releases" in newReleases.text
		assert "New Arrivals" in newReleases.text
		newReleases.click()
		try:
			genreTitle = self.driver.find_element_by_class_name("genre-title")
		except NoSuchElementException:
			self.assertTrue(False)
		return

	#@unittest.skipIf(skip,"Skipping...")
	def testdAnimated(self):
		#Verify that selecting Films: Genres: Animated from dropdown / next-level menu goes to Animated page
		self.driver.get(self.base_url + self.extension)
		try:
			filmsLink = self.driver.find_element_by_class_name("films-link")
		except NoSuchElementException:
			self.assertTrue(False)
		filmsLink.click()
		genresItem = self.driver.find_element_by_xpath("(//a[contains(text(),'Genres')])[3]")
		print(genresItem)
		assert "Genres" in genresItem.text
		filmsLink.send_keys(Keys.ESCAPE)
		for a in range(2):
			filmsLink.send_keys(Keys.ARROW_DOWN)
		animatedItem = self.driver.find_element_by_xpath("(//a[contains(text(),'Animated')])[2]")
		animatedItem.click()
		result = self.tryElementXpath("h1","Animated",1)
		self.assertTrue(result)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testeName(self): # /
		#Verify that clicking logo goes to Home page
		self.driver.get(self.base_url + self.extension)
		nameLogo = self.driver.find_element_by_class_name("name")
		nameLogo.click()
		#result = self.tryElementXpath("h1","Watch award-winning movies from around the world",1)
		#result = self.tryElementXpath("h1","Watch with us.",1)
		result = self.driver.find_element_by_xpath("(//a[contains(text(),'Watch with us.')])")
		self.assertTrue(result)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testfLogin(self): # /
		#Verify that Clicking 'Log in' link goes to Log In page
		self.driver.get(self.base_url + self.extension)
		loginLink = self.driver.find_element_by_xpath("(//a[contains(text(),'Log in')])")
		loginLink.click()
		#result = self.tryElementXpath("h1","Log in",1)
		result = self.tryElementXpath("h3","Log in",1)
		self.assertTrue(result)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testgSignup(self): #/
		#Verify that Clicking 'Start your free trial today' button goes to Register page
		self.driver.get(self.base_url + self.extension)
		#trialButton = self.driver.find_element_by_xpath("(//a[contains(text(),'Start your free trial today')])[2]")
		trialButton = self.driver.find_element_by_name("commit")

		trialButton.click()
		result = self.tryElementXpath("p","Please enter a valid email address",1)
		self.assertTrue(result)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testhDirReadMore(self): #/
		#Verify that Selecting Nina Paley: READ MORE control reveals text; READ LESS hides text
		self.driver.get(self.base_url + self.extension)
		try:
			dirMoreLink = self.driver.find_element_by_link_text("READ MORE")
		except NoSuchElementException:
			self.assertTrue(False)
		dirMoreLink.click()
		try:
			dirLessLink = self.driver.find_element_by_link_text("READ LESS")
		except NoSuchElementException:
			self.assertTrue(False)
		dirLessLink.click()
		try:
			dirMoreLink = self.driver.find_element_by_link_text("READ MORE")
		except NoSuchElementException:
			self.assertTrue(False)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testiTrailerButton(self):
		#Verify that Trailer button invokes player
		self.driver.get(self.base_url + self.extension)
		try:
			trailerButton = self.driver.find_element_by_xpath("//button[@type='button']")
		except NoSuchElementException:
			self.assertTrue(False)
		trailerButton.click()
		try:
			xButton = self.driver.find_element_by_css_selector("i.fa.fa-close")
		except NoSuchElementException:
			self.assertTrue(False)
		xButton.click()
		return

	@unittest.skipIf(skip,"Skipping...")
	def testjPlayButton(self):
		#Verify that Play button invokes player
		self.driver.get(self.base_url + self.extension)
		try:
			playButton = self.driver.find_element_by_css_selector("i.fa.fa-play")
		except NoSuchElementException:
			self.assertTrue(False)
		playButton.click()
		try:
			xButton = self.driver.find_element_by_css_selector("i.fa.fa-close")
		except NoSuchElementException:
			self.assertTrue(False)
		xButton.click()
		return

	@unittest.skipIf(skip,"Skipping...")
	def testkCast(self):
		#Verify that Clicking Cast & Crew credit link for Nina goes to Nina profile page
		self.driver.get(self.base_url + self.extension)
		try:
			castLink = self.driver.find_element_by_link_text("Cast & Crew")
		except NoSuchElementException:
			self.assertTrue(False)
		castLink.click()
		result = self.tryElementXpath("h5","Starring",1)
		self.assertTrue(result)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testlGenres(self):
		#Verify that Clicking Genres Adaptation link goes to Adaptation page
		self.driver.get(self.base_url + self.extension)
		try:
			genresLink = self.driver.find_element_by_xpath("(//a[contains(text(),'Genres')])[5]")
		except NoSuchElementException:
			self.assertTrue(False)
		for a in range(2):
			genresLink.send_keys(Keys.ARROW_DOWN)
		genresLink.click()
		try:
			adaptLink = self.driver.find_element_by_link_text("Adaptation")
		except NoSuchElementException:
			self.assertTrue(False)
		adaptLink.click()
		result = self.tryElementXpath("h1","Adaptation",1)
		self.assertTrue(result)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testqGenresNeg(self):
		#Verify that Clicking Genres Adaptation link goes to Adaptation page
		self.driver.get(self.base_url + self.extension)
		try:
			genresLink = self.driver.find_element_by_xpath("(//a[contains(text(),'Genres')])[5]")
		except NoSuchElementException:
			self.assertTrue(False)
		for a in range(2):
			genresLink.send_keys(Keys.ARROW_DOWN)
		genresLink.click()
		try:
			adaptLink = self.driver.find_element_by_link_text("Adaptation")
		except NoSuchElementException:
			self.assertTrue(False)
		try:
			castLink = self.driver.find_element_by_link_text("Cast & Crew")
		except NoSuchElementException:
			self.assertTrue(False)
		try:
			adaptLink.click()
		except NoSuchElementException:
			self.assertTrue(True)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testmFestivals(self):
		#Verify that Clicking Festivals & Awards tab shows Awards data and links
		self.driver.get(self.base_url + self.extension)
		try:
			castLink = self.driver.find_element_by_link_text("Festivals & Awards")
		except NoSuchElementException:
			self.assertTrue(False)
		castLink.click()
		result = self.tryElementXpath("h5","Festivals",1)
		self.assertTrue(result)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testnRelated(self):
		#Verify that Clicking Related Articles link goes to Keyframe page (test all links)
		self.driver.get(self.base_url + self.extension)
		try:
			relatedLink = self.driver.find_element_by_link_text("Related Articles")
		except NoSuchElementException:
			self.assertTrue(False)
		for a in range(6):
			relatedLink.send_keys(Keys.ARROW_DOWN)
		relatedLink.click()
		try:
			dailyLink = self.driver.find_element_by_xpath("(//a[contains(text(),'Daily | Most Anticipated Films of 2015')])")
		except NoSuchElementException:
			self.assertTrue(False)
		dailyLink.click()
		result = self.tryElementXpath("h1","Daily | Most Anticipated Films of 2015",1)
		self.assertTrue(result)
		return

	@unittest.skipIf(skip,"Skipping...")
	def testoFeatured(self):
		#Verify that Selecting Featured: n from dropdown goes to n page; data driven
		sel = ["Spotlights","Criterion Picks","Video Essays"]
		chk = ["Spotlight","Criterion Collection","Video Essays"]
		self.driver.get(self.base_url + self.extension)
		for ix in range(len(sel)):
			try:
				featuredLink = self.driver.find_element_by_class_name("featured-link")
			except NoSuchElementException:
				self.assertTrue(False)
			featuredLink.click()
			featuredLink.send_keys(Keys.ESCAPE)
			linkHandle = self.driver.find_element_by_xpath("(//a[contains(text(),'" + sel[ix] + "')])[2]")
			linkHandle.click()
			result = self.tryElementXpath("h1",chk[ix],1)
			self.assertTrue(result)
			self.driver.execute_script("window.history.go(-1)")
		return

	@unittest.skipIf(skip,"Skipping...")
	def testpJoin(self):
		#Verify that Clicking 'Join us:' n link goes to n page
		sel = ["Subscribe","Pricing Plans","Gift Subscriptions","Invite a Friend","Educators & Students"]
		chk = ["Sign up","Your subscription options","Do you love","Share movies you love","Resources and discounts"]
		hdr = ["h2","h1","h1","h1","h1"]
		self.driver.get(self.base_url + self.extension)
		for ix in range(len(sel)):
			linkHandle = self.driver.find_element_by_xpath("(//a[contains(text(),'" + sel[ix] + "')])")
			linkHandle.click()
			try:
				self.driver.find_element_by_xpath("(//" + hdr[ix] + "[contains(text(),'" + chk[ix] + "')])")
			except NoSuchElementException:
				self.assertTrue(False)
			self.driver.execute_script("window.history.go(-1)")
		return

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

# this is the framework calling code that will execute the entire suite and show results
if __name__ == "__main__":
	unittest.main(warnings='ignore')
