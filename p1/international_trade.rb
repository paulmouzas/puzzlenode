require 'csv'
require 'Nokogiri'

transactions = []

CSV.foreach('SAMPLE_TRANS.csv', headers: true) do |row|
  amount, currency = row['amount'].split
  transactions << { store: row['store'].to_sym, sku: row['sku'].to_sym,
    amount: amount.to_f, currency: currency.to_sym }
end

rates = {}

Nokogiri::XML(File.open('SAMPLE_RATES.xml')).css('rate').each do |node|
  from = node.css('from').text.to_sym
  rates[from] ||= []
  rates[from] << [node.css('to').text.to_sym, node.css('conversion').text.to_f]
  
end

total = 0.0

conversions = {}

transactions.each do |transaction|
  puts transaction
end