

#fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['Close'], mode='lines+markers'))
#fig.show()
"""
fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=hist.index,y=hist['Close'],name='Price'),secondary_y=False)
fig2.add_trace(go.Bar(x=hist.index,y=hist['Volume'],name='Volume'),secondary_y=True)

fig2.update_yaxes(range=[0,7000000000],secondary_y=True)
fig2.update_yaxes(visible=False, secondary_y=True)

fig2.show()"""

#fig3.add_trace(go.Bar(x=hist.index, y=hist['Volume'], name='Volume', marker={'color':hist['color']}),row=2,col=1,secondary_y=False)
#fig3.update_yaxes(range=[0,700000000],secondary_y=True)
#fig3.update_yaxes(visible=True, secondary_y=True)
#fig3.update(layout_xaxis_rangeslider_visible=False)  #hide/show range slider

#fig3.update_layout(title={'text':ticker, 'x':0.5})