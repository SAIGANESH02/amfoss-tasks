require 'nokogiri'
require 'open-uri'

puts("Enter the word which you need to produce google search results: ")

keyword = gets

doc = Nokogiri::HTML(open('https://www.google.com/search?start=0&end=11&q='+keyword))

doc.xpath('//div/a/div[text()]').each do |link|

    puts link.content

end