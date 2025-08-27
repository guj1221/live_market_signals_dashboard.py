# Advanced Buy Signals - Parameter Configurations

## Market Condition Configurations

### 🚀 Aggressive Trading (High Frequency, Higher Risk)
**Best for**: Experienced traders, volatile markets, short-term positions

```pine
// RSI Settings
rsiLength = 10
rsiOverbought = 75
rsiOversold = 25

// MACD Settings
macdFastLength = 8
macdSlowLength = 21
macdSignalLength = 5

// Bollinger Bands
bbLength = 15
bbMult = 1.8

// Volume Settings
volumeLength = 15
volumeThreshold = 1.2

// Moving Averages
emaFast = 5
emaSlow = 13
sma200 = 100

// Signal Strength Threshold
minSignalStrength = 3  // Lower threshold for more signals
```

### 🎯 Conservative Trading (Low Frequency, Lower Risk)
**Best for**: New traders, stable markets, long-term positions

```pine
// RSI Settings
rsiLength = 21
rsiOverbought = 65
rsiOversold = 35

// MACD Settings
macdFastLength = 21
macdSlowLength = 55
macdSignalLength = 13

// Bollinger Bands
bbLength = 30
bbMult = 2.5

// Volume Settings
volumeLength = 30
volumeThreshold = 2.0

// Moving Averages
emaFast = 21
emaSlow = 55
sma200 = 300

// Signal Strength Threshold
minSignalStrength = 7  // Higher threshold for fewer signals
```

### ⚖️ Balanced Trading (Medium Frequency, Medium Risk)
**Best for**: Most traders, mixed market conditions, swing trading

```pine
// RSI Settings
rsiLength = 14
rsiOverbought = 70
rsiOversold = 30

// MACD Settings
macdFastLength = 12
macdSlowLength = 26
macdSignalLength = 9

// Bollinger Bands
bbLength = 20
bbMult = 2.0

// Volume Settings
volumeLength = 20
volumeThreshold = 1.5

// Moving Averages
emaFast = 9
emaSlow = 21
sma200 = 200

// Signal Strength Threshold
minSignalStrength = 5  // Medium threshold for balanced signals
```

## Timeframe-Specific Configurations

### 📊 1-Minute to 5-Minute (Scalping)
```pine
// Fast signals for quick entries
rsiLength = 7
macdFastLength = 6
macdSlowLength = 13
bbLength = 10
emaFast = 3
emaSlow = 7
minSignalStrength = 2
```

### 📈 15-Minute to 1-Hour (Day Trading)
```pine
// Standard day trading settings
rsiLength = 14
macdFastLength = 12
macdSlowLength = 26
bbLength = 20
emaFast = 9
emaSlow = 21
minSignalStrength = 4
```

### 📊 4-Hour to Daily (Swing Trading)
```pine
// Slower, more reliable signals
rsiLength = 21
macdFastLength = 21
macdSlowLength = 55
bbLength = 30
emaFast = 21
emaSlow = 55
minSignalStrength = 6
```

### 📈 Weekly to Monthly (Position Trading)
```pine
// Long-term trend following
rsiLength = 30
macdFastLength = 30
macdSlowLength = 60
bbLength = 40
emaFast = 30
emaSlow = 60
minSignalStrength = 8
```

## Market Volatility Configurations

### 🌊 High Volatility Markets (Crypto, Penny Stocks)
```pine
// Wider bands, more sensitive signals
bbMult = 3.0
volumeThreshold = 2.0
atrMultiplier = 3.0
rsiOversold = 20
rsiOverbought = 80
```

### 🌊 Low Volatility Markets (Blue Chips, Forex Majors)
```pine
// Tighter bands, stricter signals
bbMult = 1.5
volumeThreshold = 1.2
atrMultiplier = 1.5
rsiOversold = 35
rsiOverbought = 65
```

### 🌊 Medium Volatility Markets (Most Stocks, Commodities)
```pine
// Standard settings
bbMult = 2.0
volumeThreshold = 1.5
atrMultiplier = 2.0
rsiOversold = 30
rsiOverbought = 70
```

## Trading Style Configurations

### 🎯 Momentum Trading
```pine
// Focus on strong moves
rsiLength = 10
macdFastLength = 8
emaFast = 5
volumeThreshold = 1.2
minSignalStrength = 3
```

### 🎯 Mean Reversion Trading
```pine
// Focus on oversold/overbought conditions
rsiLength = 21
bbMult = 2.5
volumeThreshold = 2.0
minSignalStrength = 6
```

### 🎯 Trend Following
```pine
// Focus on trend confirmation
emaFast = 21
emaSlow = 55
sma200 = 200
volumeThreshold = 1.5
minSignalStrength = 5
```

### 🎯 Breakout Trading
```pine
// Focus on volume and price breakouts
bbLength = 15
volumeThreshold = 2.0
rsiLength = 14
minSignalStrength = 4
```

## Risk Management Configurations

### 🛡️ Conservative Risk Management
```pine
// Tighter stops, smaller positions
atrMultiplier = 1.5
minSignalStrength = 7
requireVolumeConfirmation = true
requireTrendAlignment = true
```

### 🛡️ Moderate Risk Management
```pine
// Standard risk settings
atrMultiplier = 2.0
minSignalStrength = 5
requireVolumeConfirmation = true
requireTrendAlignment = false
```

### 🛡️ Aggressive Risk Management
```pine
// Wider stops, larger positions
atrMultiplier = 3.0
minSignalStrength = 3
requireVolumeConfirmation = false
requireTrendAlignment = false
```

## Custom Configuration Examples

### 🚀 Crypto Trading (Bitcoin, Ethereum)
```pine
// Optimized for crypto volatility
rsiLength = 12
macdFastLength = 10
macdSlowLength = 24
bbLength = 18
bbMult = 2.2
volumeThreshold = 1.8
emaFast = 7
emaSlow = 18
sma200 = 150
atrMultiplier = 2.5
minSignalStrength = 4
```

### 📈 Forex Trading (Major Pairs)
```pine
// Optimized for forex markets
rsiLength = 16
macdFastLength = 14
macdSlowLength = 28
bbLength = 22
bbMult = 1.8
volumeThreshold = 1.3
emaFast = 11
emaSlow = 23
sma200 = 250
atrMultiplier = 1.8
minSignalStrength = 5
```

### 📊 Stock Trading (Large Caps)
```pine
// Optimized for stable stocks
rsiLength = 18
macdFastLength = 16
macdSlowLength = 32
bbLength = 25
bbMult = 2.2
volumeThreshold = 1.6
emaFast = 13
emaSlow = 26
sma200 = 200
atrMultiplier = 2.0
minSignalStrength = 6
```

## Quick Setup Guide

### 1. Choose Your Trading Style
- **Scalping**: Use 1-5 minute timeframes with aggressive settings
- **Day Trading**: Use 15-60 minute timeframes with balanced settings
- **Swing Trading**: Use 4-hour to daily timeframes with conservative settings
- **Position Trading**: Use weekly to monthly timeframes with very conservative settings

### 2. Adjust for Market Conditions
- **High Volatility**: Increase ATR multiplier, volume threshold, and BB multiplier
- **Low Volatility**: Decrease ATR multiplier, volume threshold, and BB multiplier
- **Trending Markets**: Use longer moving averages and require trend alignment
- **Sideways Markets**: Use shorter moving averages and focus on mean reversion

### 3. Set Risk Parameters
- **Conservative**: Higher signal strength threshold, tighter stops
- **Moderate**: Medium signal strength threshold, standard stops
- **Aggressive**: Lower signal strength threshold, wider stops

### 4. Fine-tune Based on Results
- Start with recommended settings for your style
- Monitor performance for 20-30 trades
- Adjust parameters based on win rate and profit factor
- Keep a trading journal to track what works best

## Performance Optimization Tips

### 🚀 Speed Optimization
- Reduce calculation periods for faster performance
- Use fewer indicators if experiencing lag
- Consider using `request.security()` for multi-timeframe analysis

### 📊 Accuracy Optimization
- Use higher timeframes for more reliable signals
- Combine with fundamental analysis
- Consider market context and news events
- Use volume confirmation for all signals

### 💰 Risk Optimization
- Never risk more than 1-2% per trade
- Use position sizing based on ATR
- Set maximum daily loss limits
- Review and adjust parameters monthly