# 01_overview

Overview
Ethena is a synthetic dollar protocol built on Ethereum that provides a crypto-native solution for money not reliant on traditional banking system infrastructure, alongside a globally accessible dollar denominated rewards instrument - the 'Internet Bond'.

Ethena's synthetic dollar, USDe, provides the crypto-native, scalable solution for money achieved by delta-hedging Ethereum and Bitcoin collateral. USDe is fully-backed (subject to the discussion in the Risks section regarding events potentially resulting in loss of backing) and free to compose throughout CeFi & DeFi. 

USDe peg stability is supported through the use of delta hedging derivatives positions against  protocol-held collateral, maintaining a relatively stable value with reference to the value spot crypto assets as well as futures positions.

The 'Internet Bond' combines revenue derived from staked assets (e.g., staked Ethereum), to the extent used as backing assets, as well as the funding & basis spread from perpetual and futures markets, to create the first onchain crypto-native solution for money.

Users are currently able to:

Permissionless Acquire USDe. Access external AMM pools to acquire or dispose of USDe with assets such as USDT or USDC.

Direct Mint USDe. Deposit accepted reserve assets and receive USDe, subject to clearing KYC/KYB checks exclusively for approved market making counterparties. See Supplemental USDe Terms and Conditions.

Direct Redeem USDe. Burn USDe & receive backing assets, subject to clearing KYC/KYB checks exclusively for approved market making counterparties. See Supplemental USDe Terms and Conditions.

Stake & Unstake USDe. Receive rewards in the form of protocol revenue. Available exclusively for users in permitted jurisdictions.

# 02_problem

Problem: Crypto-Native Money
Crypto needs a decentralized base money asset, and the world has no access to a globally accessible and censorship-resistant means of holding capital.


Ethena has been built to address the largest and most obvious immediate need within crypto. 

DeFi attempts to create a parallel financial system, yet stablecoins are the most important financial instrument and remain completely tethered to, and reliant upon, traditional banking infrastructure. 

Ethena aims to provide a scalable crypto-native form of money to enable a truly independent financial system.

Crypto can no longer depend on traditional infrastructure for stablecoins 
For any functional truly independent financial system to work at scale, a reasonably stable asset not reliant on legacy banking infrastructure is required for both transactional money as well providing the core base asset for funding. Without an independent and reasonably stable reserve asset, both centralized & decentralized order books are inherently fragile.

Centralized Exchanges are in desperate need of a reliable and transparent asset for their order books, and DeFi faces ongoing existential risk by relying on USDC or RWAs with a centralized kill-switch. Reducing the reliance on the traditional banking system for the role stablecoin infrastructure plays in the space is the single most important issue facing crypto today.

8 billion people have no access to a dollar denominated means of storing capital
Whilst US citizens have access to their own $30 trillion treasury market, individuals in the rest of the world do not have permissionless access or an ability to generate a yield on a dollar denominated means of preserving capital.

User demand for existing stablecoins is already provable and enormous at $150 billion+ despite a typical “return-free" risk profile. A substantially equivalent product that provides permissionless value accrual is the largest market opportunity that crypto can provide for individuals all over the world - larger than either a volatile store of value or fiat, or RWA-backed stablecoins as they currently exist.

The most important financial instrument in the real world - a dollar denominated means of capital preservation - is a basic product everyone should have the ability to access without permission.

# 03_alternative

Alternatives: Existing Stablecoins
How to achieve scalability, censorship resistance and stability via derivatives

TLDR

Native income derived from proof-of-stake assets alongside a liquid derivatives market presents the first opportunity to utilize derivative infrastructure at scale to create scalable permissionless money, for a global independent financial settlement layer.

Existential Importance to the Space
Stablecoins are the single most important instrument in crypto. All major trading pairs across spot and futures markets in centralized and decentralized venues are denominated in stablecoin pairs with >90% of orderbook trades and >70% of onchain settlements being stablecoin denominated. Stablecoins settled >$12 trillion onchain in 2023, constitute 2 out of the 5 of the largest assets in the space, >40% of TVL in DeFi, and are by far the most utilized assets across decentralized money markets.

Stablecoins are not only the foundation of the entire industry, but are also arguably the only crypto asset to have (i) found true product-market fit globally with more than 100m users, (ii) the largest addressable market, and (iii) the greatest potential for revenue generation.


Centralized Challenges
Stablecoins dependent on traditional financial infrastructure, such as USDC or USDT, provide stability and capital efficiency, but they introduce: 

Unhedgeable custodial risk with bond collateral in regulated bank accounts which are prone to censorship.

A critical reliance upon the existing banking infrastructure and country-specific evolving regulations.

A "return-free" risk for the user as the issuer internalizes yield generated utilizing backing assets whilst exporting the risk of depeg to users.

Decentralized Fragility and Lack of Scale
"Decentralized" stablecoins - those with designs not incorporating or relying on traditional banking or financial infrastructure - have historically experienced a number of issues relating to scalability,  mechanism design, and a lack of incentives to users.

"Overcollateralized stablecoins" have historically experienced issues scaling as their growth was inexorably tied to the on-chain growth in leverage demand for Ethereum. Lately, some stablecoins have resorted to onboarding Treasuries in an effort to improve scalability, at the cost of censorship resistance.

"Algorithmic stablecoins" have faced challenges with their mechanism design which were found to be inherently fragile and unstable. Such designs are unlikely to be sustainably scalable.

Prior "delta-neutral synthetic dollars " struggled to scale due to a critical reliance on decentralized trading venues that lack sufficient liquidity and are exposed to smart contract exploits. 


The Solution is Now Possible
Question: How does one construct a trust-minimized, scalable, and reasonably stable asset which is both unreliant on the banking system and systemically creates economic protocol-level returns that can be passed to ecosystem participants?

Answer: Through the use of derivatives on backing assets (including liquid staked assets with inherent income) on deep and liquid centralized venues, USDe aims to directly address the scalability "stablecoin trilemma" that previous decentralized stablecoins designs have encountered, as well as the custodial risk deficiencies of centralized stablecoins.

# 04_solution

Solution: USDe
A crypto-native synthetic dollar utilizing spot assets as backing, onchain custody, and centralized liquidity venues

A delta-neutral synthetic dollar that is backed by assets outside the banking system and that can access centralized liquidity addresses the challenges of existing stablecoin designs.

USDe is enabled via hedging the delta of spot assets backing the token during minting. As a result, USDe provides the following benefits:

i) Scalability is achieved by utilizing derivatives which allows for USDe to scale with capital efficiency. Since the backing assets can be perfectly hedged with a short position of equivalent notional, the synthetic dollar only requires 1:1 "collateralization."

ii) Stability is supported through hedges executed against the transferred assets immediately on issuance that buttresses the synthetic USD value of USDe backing.

iii) Censorship Resistance by separating backing from the banking system and storing trustless backing assets outside of centralized liquidity venues in onchain, transparent, 24/7 auditable, programmatic custody account solutions.


Utilizing recent developments in "off-exchange" MPC secured (and similar) custody accounts to access centralized liquidity, while retaining the core value proposition of transparency and onchain custody, USDe can scale into the billions as the crypto-native dollar for both the decentralized and centralized crypto-ecosystems. As the mechanics of forming USDe backing inherently create a protocol-level revenue,  the system supports a reward-bearing 'Internet Bond' alongside USDe, sUSDe, that scales with it.

Enabling Ethereum and other digital assets to evolve into a reasonably stable medium of exchange will not only support significant capital inflows into both the centralized & decentralized ecosystems; it will also provide the most important native 'money' asset across crypto markets.

# 05_importance

Importance to the Space
Why the US Treasury is the most important financial instrument on earth
The $30tn US Treasury market is the largest, most liquid, and most important financial market on earth, acting as the foundational collateral for funding financial balance sheets, the reference pricing rate for every financial asset on earth, as well as the FX reserve asset for international sovereign entities.

This is due to its unique qualities:

Stability

Liquidity

Yield

This allows US Treasury Bonds to act as:

Transactional Money

A Store of Value and Savings Instrument

Pristine Collateral

Yet to date, an analogous asset has not existed within crypto. Why?

Why the Internet Bond can be the most important instrument in DeFi
stETH and USDC serve different roles within the DeFi ecosystem, but neither alone are the solution for a reasonably stable value-accruing collateral asset. USDC currently functions as the most important asset within DeFi, while all major exchanges are heavily reliant on USDT as quote & settlement assets for their order book markets.

This is despite their weaknesses relating to:

Centralized custody risk

Fully internalized economics: "return-free risk"

Fundamental reliance on the US Banking System

Combining the qualities of on-chain assets with a delta hedge to achieve a synthetic dollar backing for USDe allows for:

Transactional Money

Store of Value 

Reasonably Stable Backing

Censorship Resistance

The Internet Bond, sUSDe, therefore combines the relative stability of existing stablecoins with the censorship resistance of native assets. Users in permitted jurisdictions are able to stake their USDe to receive sUSDe to receive rewards generated by the protocol. USDe can therefore play an important role as a reserve asset supporting other DeFi applications that require backing (for example, stablecoin issuers) or as a collateral asset on money markets.

# 06_opportunity

Size of the Opportunity
Providing a crypto-native synthetic dollar and the first "internet bond" is not only the largest challenge in the space but the largest opportunity



Stablecoins

Stablecoins and other relatively stable, fully-backed assets intended to approximate the dollar is one of three $1 trillion+ opportunities in this space, with an immediate ~$5bn+ addressable market by embedding USDe into exchanges and capturing market share within DeFi as a reserve asset.

Ethena is agnostic to all forms of liquid staking assets (to the extent such assets are utilized as backing), off-exchange settlement providers, and sources of liquidity. The protocol is not sensitive to the competitive dynamics between providers and will benefit from the growth and innovation of the total liquid staking and derivatives ecosystems.

Internet Bonds

User demand for existing stablecoins is already provable and enormous at $150 billion+ despite their “return-free" risk profile. An asset that enables permissionless reward accrual to ecosystem participants is the largest market opportunity that crypto can provide for individuals all over the world - even larger than either a volatile store of value or stablecoins as they currently exist.

As a globally accessible and crypto-native asset, at 5bn sUSDe outstanding, sUSDe would account for less than <2bps of the US Treasury market and <0.5bps of global fixed income instruments.

# 07_ena

Use Cases
Governance

ENA is first and foremost a governance token, governing the Ethena protocol and its critical decisions. ENA holders can vote bi-annually to elect members to a Risk Committee, and in the future additional committees performing critical roles within the ecosystem. In this framework, $ENA governance tokenholders are able to delegate everyday decision-making with respect to key aspects of the ecosystem to sophisticated, expert-level stakeholders - most of whom provide advisory and similar services to other projects and protocols in the industry - while retaining transparency during the process.

Ethena's Governance discussion forum is located here.

Ethena's Snapshot ENA voting page is located here.

For the first six month term, the Risk Committee members are:

Gauntlet​

Block Analitica​

Steakhouse

Blockworks Research

LlamaRisk

Ethena Labs Research

sENA holders will be able to vote directly on ENA tokenomics proposals and any proposals concerning ENA specifically.

The community has been active with governance, with ENA holders voting on Ethereal (a perp DEX launching on the Ethena Network later this year), as well as a proposal onboarding SOL as a backing asset for USDe, and announcing the winners of the Reserve Fund RWA Allocations - which saw Blackrock's BUIDL application receiving the highest allocation.

sENA Rewards

sENA serves as the liquid receipt token for locking ENA and is composable throughout a wide range of DeFi apps. sENA itself will earn rewards, initially receiving unclaimed ENA from the season 2 airdrop distribution. 

This is intended to reward users who are more aligned to the long term growth of Ethena from more mercenary pools of capital. 

Additionally, staked ENA (sENA) now earns rewards for Ethereal. The Ethereal team committed to giving sENA holders 15% of any potential future token supply. The sENA page of our app has more details.


Restaked ENA

Generalized restaking pools in partnership with Symbiotic for staked $ENA were incorporated to add utility to $ENA, introduced to provide economic security for cross-chain transfers of USDe relying on the LayerZero DVN-based messaging system. This is the first of multiple layers of infrastructure related to the upcoming Ethena Network and financial applications built upon the chain which will utilize and benefit from restaked $ENA modules.

# 08_tokenomic

Tokenomics
Vesting Schedule

Allocation
Core Contributors

This portion of the ENA allocation (30%) represents the distribution to the Ethena Labs team and advisors who have worked on the protocol to bring USDe to market. All core contributors are locked on a 1 year 25% cliff, with 3 year linear monthly vesting thereafter. No core contributor tokens are unlocked prior to the 1yr cliff.

Investors

The investor allocation represents token rights obtained by investors backing the Ethena protocol’s development, to bootstrap both the protocol and the Reserve Fund to support Ethena’s launch. All investors are locked on a 1 year 25% cliff, with 3 year linear monthly vesting thereafter. No investor tokens are unlocked prior to the 1yr cliff.

Foundation

The Foundation allocation will be used to further initiatives that serve to widen the reach of USDe, reducing crypto’s reliance on traditional banking rails and fiat-backed centralized stablecoins. This ENA will be used to fund further development, risk assessments, audits and much more.

Ecosystem Development and Airdrops

30% of ENA is allocated to developing the Ethena ecosystem. The first 10% represents the portion of ENA airdropped to Ethena users as part of the first and second seasons of the Rewards Campaigns. The remainder of the allocation will be used for various Ethena initiatives, including the upcoming second season of the incentive campaign, as well as various cross chain initiatives, exchange partnerships and much more, which will be held by a DAO controlled multisig.

# aggregated

# 01_overview

Overview
Ethena is a synthetic dollar protocol built on Ethereum that provides a crypto-native solution for money not reliant on traditional banking system infrastructure, alongside a globally accessible dollar denominated rewards instrument - the 'Internet Bond'.

Ethena's synthetic dollar, USDe, provides the crypto-native, scalable solution for money achieved by delta-hedging Ethereum and Bitcoin collateral. USDe is fully-backed (subject to the discussion in the Risks section regarding events potentially resulting in loss of backing) and free to compose throughout CeFi & DeFi. 

USDe peg stability is supported through the use of delta hedging derivatives positions against  protocol-held collateral, maintaining a relatively stable value with reference to the value spot crypto assets as well as futures positions.

The 'Internet Bond' combines revenue derived from staked assets (e.g., staked Ethereum), to the extent used as backing assets, as well as the funding & basis spread from perpetual and futures markets, to create the first onchain crypto-native solution for money.

Users are currently able to:

Permissionless Acquire USDe. Access external AMM pools to acquire or dispose of USDe with assets such as USDT or USDC.

Direct Mint USDe. Deposit accepted reserve assets and receive USDe, subject to clearing KYC/KYB checks exclusively for approved market making counterparties. See Supplemental USDe Terms and Conditions.

Direct Redeem USDe. Burn USDe & receive backing assets, subject to clearing KYC/KYB checks exclusively for approved market making counterparties. See Supplemental USDe Terms and Conditions.

Stake & Unstake USDe. Receive rewards in the form of protocol revenue. Available exclusively for users in permitted jurisdictions.

# 02_problem

Problem: Crypto-Native Money
Crypto needs a decentralized base money asset, and the world has no access to a globally accessible and censorship-resistant means of holding capital.


Ethena has been built to address the largest and most obvious immediate need within crypto. 

DeFi attempts to create a parallel financial system, yet stablecoins are the most important financial instrument and remain completely tethered to, and reliant upon, traditional banking infrastructure. 

Ethena aims to provide a scalable crypto-native form of money to enable a truly independent financial system.

Crypto can no longer depend on traditional infrastructure for stablecoins 
For any functional truly independent financial system to work at scale, a reasonably stable asset not reliant on legacy banking infrastructure is required for both transactional money as well providing the core base asset for funding. Without an independent and reasonably stable reserve asset, both centralized & decentralized order books are inherently fragile.

Centralized Exchanges are in desperate need of a reliable and transparent asset for their order books, and DeFi faces ongoing existential risk by relying on USDC or RWAs with a centralized kill-switch. Reducing the reliance on the traditional banking system for the role stablecoin infrastructure plays in the space is the single most important issue facing crypto today.

8 billion people have no access to a dollar denominated means of storing capital
Whilst US citizens have access to their own $30 trillion treasury market, individuals in the rest of the world do not have permissionless access or an ability to generate a yield on a dollar denominated means of preserving capital.

User demand for existing stablecoins is already provable and enormous at $150 billion+ despite a typical “return-free" risk profile. A substantially equivalent product that provides permissionless value accrual is the largest market opportunity that crypto can provide for individuals all over the world - larger than either a volatile store of value or fiat, or RWA-backed stablecoins as they currently exist.

The most important financial instrument in the real world - a dollar denominated means of capital preservation - is a basic product everyone should have the ability to access without permission.

# 03_alternative

Alternatives: Existing Stablecoins
How to achieve scalability, censorship resistance and stability via derivatives

TLDR

Native income derived from proof-of-stake assets alongside a liquid derivatives market presents the first opportunity to utilize derivative infrastructure at scale to create scalable permissionless money, for a global independent financial settlement layer.

Existential Importance to the Space
Stablecoins are the single most important instrument in crypto. All major trading pairs across spot and futures markets in centralized and decentralized venues are denominated in stablecoin pairs with >90% of orderbook trades and >70% of onchain settlements being stablecoin denominated. Stablecoins settled >$12 trillion onchain in 2023, constitute 2 out of the 5 of the largest assets in the space, >40% of TVL in DeFi, and are by far the most utilized assets across decentralized money markets.

Stablecoins are not only the foundation of the entire industry, but are also arguably the only crypto asset to have (i) found true product-market fit globally with more than 100m users, (ii) the largest addressable market, and (iii) the greatest potential for revenue generation.


Centralized Challenges
Stablecoins dependent on traditional financial infrastructure, such as USDC or USDT, provide stability and capital efficiency, but they introduce: 

Unhedgeable custodial risk with bond collateral in regulated bank accounts which are prone to censorship.

A critical reliance upon the existing banking infrastructure and country-specific evolving regulations.

A "return-free" risk for the user as the issuer internalizes yield generated utilizing backing assets whilst exporting the risk of depeg to users.

Decentralized Fragility and Lack of Scale
"Decentralized" stablecoins - those with designs not incorporating or relying on traditional banking or financial infrastructure - have historically experienced a number of issues relating to scalability,  mechanism design, and a lack of incentives to users.

"Overcollateralized stablecoins" have historically experienced issues scaling as their growth was inexorably tied to the on-chain growth in leverage demand for Ethereum. Lately, some stablecoins have resorted to onboarding Treasuries in an effort to improve scalability, at the cost of censorship resistance.

"Algorithmic stablecoins" have faced challenges with their mechanism design which were found to be inherently fragile and unstable. Such designs are unlikely to be sustainably scalable.

Prior "delta-neutral synthetic dollars " struggled to scale due to a critical reliance on decentralized trading venues that lack sufficient liquidity and are exposed to smart contract exploits. 


The Solution is Now Possible
Question: How does one construct a trust-minimized, scalable, and reasonably stable asset which is both unreliant on the banking system and systemically creates economic protocol-level returns that can be passed to ecosystem participants?

Answer: Through the use of derivatives on backing assets (including liquid staked assets with inherent income) on deep and liquid centralized venues, USDe aims to directly address the scalability "stablecoin trilemma" that previous decentralized stablecoins designs have encountered, as well as the custodial risk deficiencies of centralized stablecoins.

# 04_solution

Solution: USDe
A crypto-native synthetic dollar utilizing spot assets as backing, onchain custody, and centralized liquidity venues

A delta-neutral synthetic dollar that is backed by assets outside the banking system and that can access centralized liquidity addresses the challenges of existing stablecoin designs.

USDe is enabled via hedging the delta of spot assets backing the token during minting. As a result, USDe provides the following benefits:

i) Scalability is achieved by utilizing derivatives which allows for USDe to scale with capital efficiency. Since the backing assets can be perfectly hedged with a short position of equivalent notional, the synthetic dollar only requires 1:1 "collateralization."

ii) Stability is supported through hedges executed against the transferred assets immediately on issuance that buttresses the synthetic USD value of USDe backing.

iii) Censorship Resistance by separating backing from the banking system and storing trustless backing assets outside of centralized liquidity venues in onchain, transparent, 24/7 auditable, programmatic custody account solutions.


Utilizing recent developments in "off-exchange" MPC secured (and similar) custody accounts to access centralized liquidity, while retaining the core value proposition of transparency and onchain custody, USDe can scale into the billions as the crypto-native dollar for both the decentralized and centralized crypto-ecosystems. As the mechanics of forming USDe backing inherently create a protocol-level revenue,  the system supports a reward-bearing 'Internet Bond' alongside USDe, sUSDe, that scales with it.

Enabling Ethereum and other digital assets to evolve into a reasonably stable medium of exchange will not only support significant capital inflows into both the centralized & decentralized ecosystems; it will also provide the most important native 'money' asset across crypto markets.

# 05_importance

Importance to the Space
Why the US Treasury is the most important financial instrument on earth
The $30tn US Treasury market is the largest, most liquid, and most important financial market on earth, acting as the foundational collateral for funding financial balance sheets, the reference pricing rate for every financial asset on earth, as well as the FX reserve asset for international sovereign entities.

This is due to its unique qualities:

Stability

Liquidity

Yield

This allows US Treasury Bonds to act as:

Transactional Money

A Store of Value and Savings Instrument

Pristine Collateral

Yet to date, an analogous asset has not existed within crypto. Why?

Why the Internet Bond can be the most important instrument in DeFi
stETH and USDC serve different roles within the DeFi ecosystem, but neither alone are the solution for a reasonably stable value-accruing collateral asset. USDC currently functions as the most important asset within DeFi, while all major exchanges are heavily reliant on USDT as quote & settlement assets for their order book markets.

This is despite their weaknesses relating to:

Centralized custody risk

Fully internalized economics: "return-free risk"

Fundamental reliance on the US Banking System

Combining the qualities of on-chain assets with a delta hedge to achieve a synthetic dollar backing for USDe allows for:

Transactional Money

Store of Value 

Reasonably Stable Backing

Censorship Resistance

The Internet Bond, sUSDe, therefore combines the relative stability of existing stablecoins with the censorship resistance of native assets. Users in permitted jurisdictions are able to stake their USDe to receive sUSDe to receive rewards generated by the protocol. USDe can therefore play an important role as a reserve asset supporting other DeFi applications that require backing (for example, stablecoin issuers) or as a collateral asset on money markets.

# 06_opportunity

Size of the Opportunity
Providing a crypto-native synthetic dollar and the first "internet bond" is not only the largest challenge in the space but the largest opportunity



Stablecoins

Stablecoins and other relatively stable, fully-backed assets intended to approximate the dollar is one of three $1 trillion+ opportunities in this space, with an immediate ~$5bn+ addressable market by embedding USDe into exchanges and capturing market share within DeFi as a reserve asset.

Ethena is agnostic to all forms of liquid staking assets (to the extent such assets are utilized as backing), off-exchange settlement providers, and sources of liquidity. The protocol is not sensitive to the competitive dynamics between providers and will benefit from the growth and innovation of the total liquid staking and derivatives ecosystems.

Internet Bonds

User demand for existing stablecoins is already provable and enormous at $150 billion+ despite their “return-free" risk profile. An asset that enables permissionless reward accrual to ecosystem participants is the largest market opportunity that crypto can provide for individuals all over the world - even larger than either a volatile store of value or stablecoins as they currently exist.

As a globally accessible and crypto-native asset, at 5bn sUSDe outstanding, sUSDe would account for less than <2bps of the US Treasury market and <0.5bps of global fixed income instruments.

# 07_ena

Use Cases
Governance

ENA is first and foremost a governance token, governing the Ethena protocol and its critical decisions. ENA holders can vote bi-annually to elect members to a Risk Committee, and in the future additional committees performing critical roles within the ecosystem. In this framework, $ENA governance tokenholders are able to delegate everyday decision-making with respect to key aspects of the ecosystem to sophisticated, expert-level stakeholders - most of whom provide advisory and similar services to other projects and protocols in the industry - while retaining transparency during the process.

Ethena's Governance discussion forum is located here.

Ethena's Snapshot ENA voting page is located here.

For the first six month term, the Risk Committee members are:

Gauntlet​

Block Analitica​

Steakhouse

Blockworks Research

LlamaRisk

Ethena Labs Research

sENA holders will be able to vote directly on ENA tokenomics proposals and any proposals concerning ENA specifically.

The community has been active with governance, with ENA holders voting on Ethereal (a perp DEX launching on the Ethena Network later this year), as well as a proposal onboarding SOL as a backing asset for USDe, and announcing the winners of the Reserve Fund RWA Allocations - which saw Blackrock's BUIDL application receiving the highest allocation.

sENA Rewards

sENA serves as the liquid receipt token for locking ENA and is composable throughout a wide range of DeFi apps. sENA itself will earn rewards, initially receiving unclaimed ENA from the season 2 airdrop distribution. 

This is intended to reward users who are more aligned to the long term growth of Ethena from more mercenary pools of capital. 

Additionally, staked ENA (sENA) now earns rewards for Ethereal. The Ethereal team committed to giving sENA holders 15% of any potential future token supply. The sENA page of our app has more details.


Restaked ENA

Generalized restaking pools in partnership with Symbiotic for staked $ENA were incorporated to add utility to $ENA, introduced to provide economic security for cross-chain transfers of USDe relying on the LayerZero DVN-based messaging system. This is the first of multiple layers of infrastructure related to the upcoming Ethena Network and financial applications built upon the chain which will utilize and benefit from restaked $ENA modules.

# 08_tokenomic

Tokenomics
Vesting Schedule

Allocation
Core Contributors

This portion of the ENA allocation (30%) represents the distribution to the Ethena Labs team and advisors who have worked on the protocol to bring USDe to market. All core contributors are locked on a 1 year 25% cliff, with 3 year linear monthly vesting thereafter. No core contributor tokens are unlocked prior to the 1yr cliff.

Investors

The investor allocation represents token rights obtained by investors backing the Ethena protocol’s development, to bootstrap both the protocol and the Reserve Fund to support Ethena’s launch. All investors are locked on a 1 year 25% cliff, with 3 year linear monthly vesting thereafter. No investor tokens are unlocked prior to the 1yr cliff.

Foundation

The Foundation allocation will be used to further initiatives that serve to widen the reach of USDe, reducing crypto’s reliance on traditional banking rails and fiat-backed centralized stablecoins. This ENA will be used to fund further development, risk assessments, audits and much more.

Ecosystem Development and Airdrops

30% of ENA is allocated to developing the Ethena ecosystem. The first 10% represents the portion of ENA airdropped to Ethena users as part of the first and second seasons of the Rewards Campaigns. The remainder of the allocation will be used for various Ethena initiatives, including the upcoming second season of the incentive campaign, as well as various cross chain initiatives, exchange partnerships and much more, which will be held by a DAO controlled multisig.

# aggregated

# alternative

Alternatives: Existing Stablecoins
How to achieve scalability, censorship resistance and stability via derivatives

TLDR

Native income derived from proof-of-stake assets alongside a liquid derivatives market presents the first opportunity to utilize derivative infrastructure at scale to create scalable permissionless money, for a global independent financial settlement layer.

Existential Importance to the Space
Stablecoins are the single most important instrument in crypto. All major trading pairs across spot and futures markets in centralized and decentralized venues are denominated in stablecoin pairs with >90% of orderbook trades and >70% of onchain settlements being stablecoin denominated. Stablecoins settled >$12 trillion onchain in 2023, constitute 2 out of the 5 of the largest assets in the space, >40% of TVL in DeFi, and are by far the most utilized assets across decentralized money markets.

Stablecoins are not only the foundation of the entire industry, but are also arguably the only crypto asset to have (i) found true product-market fit globally with more than 100m users, (ii) the largest addressable market, and (iii) the greatest potential for revenue generation.


Centralized Challenges
Stablecoins dependent on traditional financial infrastructure, such as USDC or USDT, provide stability and capital efficiency, but they introduce: 

Unhedgeable custodial risk with bond collateral in regulated bank accounts which are prone to censorship.

A critical reliance upon the existing banking infrastructure and country-specific evolving regulations.

A "return-free" risk for the user as the issuer internalizes yield generated utilizing backing assets whilst exporting the risk of depeg to users.

Decentralized Fragility and Lack of Scale
"Decentralized" stablecoins - those with designs not incorporating or relying on traditional banking or financial infrastructure - have historically experienced a number of issues relating to scalability,  mechanism design, and a lack of incentives to users.

"Overcollateralized stablecoins" have historically experienced issues scaling as their growth was inexorably tied to the on-chain growth in leverage demand for Ethereum. Lately, some stablecoins have resorted to onboarding Treasuries in an effort to improve scalability, at the cost of censorship resistance.

"Algorithmic stablecoins" have faced challenges with their mechanism design which were found to be inherently fragile and unstable. Such designs are unlikely to be sustainably scalable.

Prior "delta-neutral synthetic dollars " struggled to scale due to a critical reliance on decentralized trading venues that lack sufficient liquidity and are exposed to smart contract exploits. 


The Solution is Now Possible
Question: How does one construct a trust-minimized, scalable, and reasonably stable asset which is both unreliant on the banking system and systemically creates economic protocol-level returns that can be passed to ecosystem participants?

Answer: Through the use of derivatives on backing assets (including liquid staked assets with inherent income) on deep and liquid centralized venues, USDe aims to directly address the scalability "stablecoin trilemma" that previous decentralized stablecoins designs have encountered, as well as the custodial risk deficiencies of centralized stablecoins.

# ena

Use Cases
Governance

ENA is first and foremost a governance token, governing the Ethena protocol and its critical decisions. ENA holders can vote bi-annually to elect members to a Risk Committee, and in the future additional committees performing critical roles within the ecosystem. In this framework, $ENA governance tokenholders are able to delegate everyday decision-making with respect to key aspects of the ecosystem to sophisticated, expert-level stakeholders - most of whom provide advisory and similar services to other projects and protocols in the industry - while retaining transparency during the process.

Ethena's Governance discussion forum is located here.

Ethena's Snapshot ENA voting page is located here.

For the first six month term, the Risk Committee members are:

Gauntlet​

Block Analitica​

Steakhouse

Blockworks Research

LlamaRisk

Ethena Labs Research

sENA holders will be able to vote directly on ENA tokenomics proposals and any proposals concerning ENA specifically.

The community has been active with governance, with ENA holders voting on Ethereal (a perp DEX launching on the Ethena Network later this year), as well as a proposal onboarding SOL as a backing asset for USDe, and announcing the winners of the Reserve Fund RWA Allocations - which saw Blackrock's BUIDL application receiving the highest allocation.

sENA Rewards

sENA serves as the liquid receipt token for locking ENA and is composable throughout a wide range of DeFi apps. sENA itself will earn rewards, initially receiving unclaimed ENA from the season 2 airdrop distribution. 

This is intended to reward users who are more aligned to the long term growth of Ethena from more mercenary pools of capital. 

Additionally, staked ENA (sENA) now earns rewards for Ethereal. The Ethereal team committed to giving sENA holders 15% of any potential future token supply. The sENA page of our app has more details.


Restaked ENA

Generalized restaking pools in partnership with Symbiotic for staked $ENA were incorporated to add utility to $ENA, introduced to provide economic security for cross-chain transfers of USDe relying on the LayerZero DVN-based messaging system. This is the first of multiple layers of infrastructure related to the upcoming Ethena Network and financial applications built upon the chain which will utilize and benefit from restaked $ENA modules.

# importance

Importance to the Space
Why the US Treasury is the most important financial instrument on earth
The $30tn US Treasury market is the largest, most liquid, and most important financial market on earth, acting as the foundational collateral for funding financial balance sheets, the reference pricing rate for every financial asset on earth, as well as the FX reserve asset for international sovereign entities.

This is due to its unique qualities:

Stability

Liquidity

Yield

This allows US Treasury Bonds to act as:

Transactional Money

A Store of Value and Savings Instrument

Pristine Collateral

Yet to date, an analogous asset has not existed within crypto. Why?

Why the Internet Bond can be the most important instrument in DeFi
stETH and USDC serve different roles within the DeFi ecosystem, but neither alone are the solution for a reasonably stable value-accruing collateral asset. USDC currently functions as the most important asset within DeFi, while all major exchanges are heavily reliant on USDT as quote & settlement assets for their order book markets.

This is despite their weaknesses relating to:

Centralized custody risk

Fully internalized economics: "return-free risk"

Fundamental reliance on the US Banking System

Combining the qualities of on-chain assets with a delta hedge to achieve a synthetic dollar backing for USDe allows for:

Transactional Money

Store of Value 

Reasonably Stable Backing

Censorship Resistance

The Internet Bond, sUSDe, therefore combines the relative stability of existing stablecoins with the censorship resistance of native assets. Users in permitted jurisdictions are able to stake their USDe to receive sUSDe to receive rewards generated by the protocol. USDe can therefore play an important role as a reserve asset supporting other DeFi applications that require backing (for example, stablecoin issuers) or as a collateral asset on money markets.

# opportunity

Size of the Opportunity
Providing a crypto-native synthetic dollar and the first "internet bond" is not only the largest challenge in the space but the largest opportunity



Stablecoins

Stablecoins and other relatively stable, fully-backed assets intended to approximate the dollar is one of three $1 trillion+ opportunities in this space, with an immediate ~$5bn+ addressable market by embedding USDe into exchanges and capturing market share within DeFi as a reserve asset.

Ethena is agnostic to all forms of liquid staking assets (to the extent such assets are utilized as backing), off-exchange settlement providers, and sources of liquidity. The protocol is not sensitive to the competitive dynamics between providers and will benefit from the growth and innovation of the total liquid staking and derivatives ecosystems.

Internet Bonds

User demand for existing stablecoins is already provable and enormous at $150 billion+ despite their “return-free" risk profile. An asset that enables permissionless reward accrual to ecosystem participants is the largest market opportunity that crypto can provide for individuals all over the world - even larger than either a volatile store of value or stablecoins as they currently exist.

As a globally accessible and crypto-native asset, at 5bn sUSDe outstanding, sUSDe would account for less than <2bps of the US Treasury market and <0.5bps of global fixed income instruments.

# overview

Overview
Ethena is a synthetic dollar protocol built on Ethereum that provides a crypto-native solution for money not reliant on traditional banking system infrastructure, alongside a globally accessible dollar denominated rewards instrument - the 'Internet Bond'.

Ethena's synthetic dollar, USDe, provides the crypto-native, scalable solution for money achieved by delta-hedging Ethereum and Bitcoin collateral. USDe is fully-backed (subject to the discussion in the Risks section regarding events potentially resulting in loss of backing) and free to compose throughout CeFi & DeFi. 

USDe peg stability is supported through the use of delta hedging derivatives positions against  protocol-held collateral, maintaining a relatively stable value with reference to the value spot crypto assets as well as futures positions.

The 'Internet Bond' combines revenue derived from staked assets (e.g., staked Ethereum), to the extent used as backing assets, as well as the funding & basis spread from perpetual and futures markets, to create the first onchain crypto-native solution for money.

Users are currently able to:

Permissionless Acquire USDe. Access external AMM pools to acquire or dispose of USDe with assets such as USDT or USDC.

Direct Mint USDe. Deposit accepted reserve assets and receive USDe, subject to clearing KYC/KYB checks exclusively for approved market making counterparties. See Supplemental USDe Terms and Conditions.

Direct Redeem USDe. Burn USDe & receive backing assets, subject to clearing KYC/KYB checks exclusively for approved market making counterparties. See Supplemental USDe Terms and Conditions.

Stake & Unstake USDe. Receive rewards in the form of protocol revenue. Available exclusively for users in permitted jurisdictions.

# problem

Problem: Crypto-Native Money
Crypto needs a decentralized base money asset, and the world has no access to a globally accessible and censorship-resistant means of holding capital.


Ethena has been built to address the largest and most obvious immediate need within crypto. 

DeFi attempts to create a parallel financial system, yet stablecoins are the most important financial instrument and remain completely tethered to, and reliant upon, traditional banking infrastructure. 

Ethena aims to provide a scalable crypto-native form of money to enable a truly independent financial system.

Crypto can no longer depend on traditional infrastructure for stablecoins 
For any functional truly independent financial system to work at scale, a reasonably stable asset not reliant on legacy banking infrastructure is required for both transactional money as well providing the core base asset for funding. Without an independent and reasonably stable reserve asset, both centralized & decentralized order books are inherently fragile.

Centralized Exchanges are in desperate need of a reliable and transparent asset for their order books, and DeFi faces ongoing existential risk by relying on USDC or RWAs with a centralized kill-switch. Reducing the reliance on the traditional banking system for the role stablecoin infrastructure plays in the space is the single most important issue facing crypto today.

8 billion people have no access to a dollar denominated means of storing capital
Whilst US citizens have access to their own $30 trillion treasury market, individuals in the rest of the world do not have permissionless access or an ability to generate a yield on a dollar denominated means of preserving capital.

User demand for existing stablecoins is already provable and enormous at $150 billion+ despite a typical “return-free" risk profile. A substantially equivalent product that provides permissionless value accrual is the largest market opportunity that crypto can provide for individuals all over the world - larger than either a volatile store of value or fiat, or RWA-backed stablecoins as they currently exist.

The most important financial instrument in the real world - a dollar denominated means of capital preservation - is a basic product everyone should have the ability to access without permission.

# solution

Solution: USDe
A crypto-native synthetic dollar utilizing spot assets as backing, onchain custody, and centralized liquidity venues

A delta-neutral synthetic dollar that is backed by assets outside the banking system and that can access centralized liquidity addresses the challenges of existing stablecoin designs.

USDe is enabled via hedging the delta of spot assets backing the token during minting. As a result, USDe provides the following benefits:

i) Scalability is achieved by utilizing derivatives which allows for USDe to scale with capital efficiency. Since the backing assets can be perfectly hedged with a short position of equivalent notional, the synthetic dollar only requires 1:1 "collateralization."

ii) Stability is supported through hedges executed against the transferred assets immediately on issuance that buttresses the synthetic USD value of USDe backing.

iii) Censorship Resistance by separating backing from the banking system and storing trustless backing assets outside of centralized liquidity venues in onchain, transparent, 24/7 auditable, programmatic custody account solutions.


Utilizing recent developments in "off-exchange" MPC secured (and similar) custody accounts to access centralized liquidity, while retaining the core value proposition of transparency and onchain custody, USDe can scale into the billions as the crypto-native dollar for both the decentralized and centralized crypto-ecosystems. As the mechanics of forming USDe backing inherently create a protocol-level revenue,  the system supports a reward-bearing 'Internet Bond' alongside USDe, sUSDe, that scales with it.

Enabling Ethereum and other digital assets to evolve into a reasonably stable medium of exchange will not only support significant capital inflows into both the centralized & decentralized ecosystems; it will also provide the most important native 'money' asset across crypto markets.

# tokenomic

Tokenomics
Vesting Schedule

Allocation
Core Contributors

This portion of the ENA allocation (30%) represents the distribution to the Ethena Labs team and advisors who have worked on the protocol to bring USDe to market. All core contributors are locked on a 1 year 25% cliff, with 3 year linear monthly vesting thereafter. No core contributor tokens are unlocked prior to the 1yr cliff.

Investors

The investor allocation represents token rights obtained by investors backing the Ethena protocol’s development, to bootstrap both the protocol and the Reserve Fund to support Ethena’s launch. All investors are locked on a 1 year 25% cliff, with 3 year linear monthly vesting thereafter. No investor tokens are unlocked prior to the 1yr cliff.

Foundation

The Foundation allocation will be used to further initiatives that serve to widen the reach of USDe, reducing crypto’s reliance on traditional banking rails and fiat-backed centralized stablecoins. This ENA will be used to fund further development, risk assessments, audits and much more.

Ecosystem Development and Airdrops

30% of ENA is allocated to developing the Ethena ecosystem. The first 10% represents the portion of ENA airdropped to Ethena users as part of the first and second seasons of the Rewards Campaigns. The remainder of the allocation will be used for various Ethena initiatives, including the upcoming second season of the incentive campaign, as well as various cross chain initiatives, exchange partnerships and much more, which will be held by a DAO controlled multisig.


