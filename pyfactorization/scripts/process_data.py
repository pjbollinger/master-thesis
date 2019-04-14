import pandas

df = pandas.read_csv('./generated_data/generated_data_regular_array_multiplier.csv')
data = 100*df['resolved_count']/df['total_count']
data.index += 2
data.index *= 2
print(data)
plot = data.plot(title="Bits Deduced Decreases as Size of Semiprime Increases", logy=True, logx=True)
plot.set_xlabel("Size of Semiprime (Bits)")
plot.set_ylabel("Bits Deduced (%)")
fig = plot.get_figure()
fig.savefig("./generated_data/output.png")

data.to_csv('./generated_data/test.csv')
