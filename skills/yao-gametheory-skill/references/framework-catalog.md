# Game Theory Framework Catalog And AI Router

This catalog is the skill's applied framework library. Use it to choose and combine game theory frames before writing a CEO strategy report.

## Operating Principle

Do not pick a famous framework first. Read the user's case and route by strategic structure:

- who can react
- whether moves are simultaneous or sequential
- whether information is complete or incomplete
- whether the interaction repeats
- whether binding contracts, commitments, signals, alliances, auctions, or market structure matter
- what payoff dimensions drive behavior

A practical report normally uses:

- `1` primary framework: the main structure of the game
- `2-4` secondary lenses: checks for equilibrium, commitment, information, repetition, coalition, or market-competition effects
- `1` output format: opponent reaction map, payoff matrix, scenario tree, bargaining range, auction map, or coalition map

## AI Application Router

### Step 1: Detect The Strategic Structure

Route by input signals:

- price, margin, discount, SKU parity -> Bertrand, price war, prisoner dilemma, repeated game
- capacity, output, supply, quantity, market share -> Cournot, capacity commitment, Stackelberg
- first mover, roadmap, entry, retaliation, threat -> sequential game, entry deterrence, subgame perfection
- negotiation, financing, terms, BATNA, reservation value -> bargaining game, ultimatum, outside-option analysis
- M&A bid, procurement, scarce slot, ad auction, tender -> auction or bidding game
- alliance, channel, ecosystem, standard, partner defection -> coalition game, coordination game, repeated game
- signal, announcement, free version, public roadmap, regulatory posture -> signaling game, cheap talk, credible commitment
- hidden type, private information, adverse selection -> Bayesian game, screening, signaling
- trust, cooperation, repeated vendors, channel discipline -> repeated game, prisoner dilemma, stag hunt
- winner-take-all, platform, network effects -> coordination, tipping, platform governance, multi-sided game
- regulator, public authority, enforcement, compliance -> sequential game, signaling, mechanism design, repeated reputation

### Step 2: Choose Primary Framework

Use the primary framework that explains the first-order payoff movement:

- if one action pair can be scored clearly, use normal-form or payoff-matrix game
- if timing changes incentives, use sequential or extensive-form game
- if future retaliation or trust changes today's move, use repeated game
- if private information changes behavior, use Bayesian or signaling game
- if surplus split is the core problem, use bargaining
- if price or quantity competition is central, use Bertrand, Cournot, or Stackelberg
- if multiple parties can form blocks, use coalition game

### Step 3: Add Secondary Lenses

Add secondary lenses only when they change the recommendation:

- Nash equilibrium: check whether each player is best responding.
- Subgame perfection: remove non-credible threats.
- Commitment: test whether our move is costly, observable, hard to reverse, incentive-compatible, and capability-backed.
- Signaling: test whether public statements or launches are costly to fake.
- Repeated game: check whether future surplus sustains cooperation or punishment.
- Coordination: check whether players may get stuck in a bad convention.
- Zero-sum: check whether value creation is impossible and conflict is purely distributive.
- Regulation and ethics: flag tactics that need legal or compliance review.

### Step 4: Combine Frameworks

Use these default combinations:

- price war: Bertrand + prisoner dilemma + repeated game + credible commitment
- channel conflict: coalition game + repeated game + bargaining + signaling
- platform ecosystem: coordination + network effects + coalition game + mechanism design
- M&A竞价: auction + bargaining + signaling + winner's curse
- financing negotiation: bargaining + signaling + outside option + sequential concession game
- competitor free version: signaling + Bertrand + entry deterrence + repeated game
- regulator communication: sequential game + signaling + mechanism design + reputation
- market entry: entry deterrence + Stackelberg + credible threat + incomplete information
- standard-setting alliance: coordination + coalition game + repeated game + hold-up risk

## Framework Catalog

### Foundational Concepts

#### Players, Strategies, Payoffs

- when to use: every game.
- player structure: all parties whose choices can change the outcome.
- CEO scenarios: pricing, channel deals, financing, platform rules, regulatory engagement.
- output checks: name players, feasible strategies, payoff basis, data status, and missing information.

#### Normal-Form Game

- when to use: moves are effectively simultaneous or timing is not the main issue.
- player structure: two or more players choose from discrete strategies.
- CEO scenarios: price response, launch timing, feature parity, channel incentive choice.
- output checks: payoff matrix, dominated strategies, best responses, Nash candidates.

#### Extensive-Form / Sequential Game

- when to use: order of moves matters.
- player structure: first mover, follower, possible later responders.
- CEO scenarios: entry deterrence, public roadmap, retaliation threat, staged negotiation.
- output checks: game tree, backward induction, credible threat test, subgame-perfect logic.

#### Nash Equilibrium / 纳什均衡

- when to use: test whether a predicted outcome is stable because no player wants to unilaterally deviate.
- player structure: every player has a strategy and payoff ranking.
- CEO scenarios: price war, channel matching, platform fee setting, supplier terms.
- output checks: identify each player's best response, show whether the action profile is stable, note multiple equilibria or no pure equilibrium.

#### Dominant Strategy / 占优策略

- when to use: one action is best regardless of others' actions.
- player structure: at least one player has clearly ranked payoffs across opponent actions.
- CEO scenarios: "always match price", "always reject bad terms", "always comply publicly".
- output checks: prove the action beats alternatives across all modeled responses; avoid calling a weak heuristic dominant.

#### Mixed Strategy / 混合策略

- when to use: pure predictability can be exploited or no pure equilibrium exists.
- player structure: players randomize or keep ambiguity across actions.
- CEO scenarios: unpredictable promotions, selective bidding, staggered feature releases, negotiation concession timing.
- output checks: explain why ambiguity is valuable, define randomization or discretion rule, avoid fake precision.

#### Correlated / Focal-Point Coordination / 相关均衡与焦点协调

- when to use: players may coordinate around conventions, signals, standards, or market anchors.
- player structure: multiple players benefit from matching expectations.
- CEO scenarios: platform standard, channel policy, pricing convention, industry communication.
- output checks: identify focal point, who observes it, why deviation is costly, whether another focal point can replace it.

### Classic Two-Player Matrix Games

#### Prisoner's Dilemma / 囚徒困境

- when to use: mutual cooperation is better for both, but each side has a short-term incentive to defect.
- player structure: two or more parties can cooperate or defect.
- CEO scenarios: price war, channel discipline, data-sharing alliance, vendor quality, marketplace governance.
- output checks: show temptation payoff, mutual-cooperation payoff, mutual-defection payoff, and repeated-game mechanisms that can sustain cooperation.

#### Zero-Sum Game / 零和博弈

- when to use: one player's gain is roughly another player's loss and total surplus cannot be expanded.
- player structure: direct adversaries with opposed payoffs.
- CEO scenarios: fixed-budget procurement, winner-take-all bid, scarce license, exclusive channel slot.
- output checks: verify the game is truly zero-sum; if value creation or relationship value exists, downgrade to mixed-motive game.

#### Non-Zero-Sum / Mixed-Motive Game / 非零和与混合动机博弈

- when to use: players compete and can still create joint surplus.
- player structure: players have both conflict and cooperation incentives.
- CEO scenarios: platform partners, channel co-selling, joint venture, regulated industry negotiation.
- output checks: separate distributive value capture from cooperative value creation.

#### Coordination Game / 协调博弈

- when to use: players mainly need to choose compatible actions.
- player structure: multiple players prefer matching or converging.
- CEO scenarios: standard setting, ecosystem migration, internal cross-functional rollout, marketplace rule adoption.
- output checks: identify good and bad equilibria, switching cost, focal points, and coordination mechanism.

#### Stag Hunt / Assurance Game / 猎鹿博弈

- when to use: high-upside cooperation is best, but each player fears being the only cooperator.
- player structure: players choose safe solo action or risky cooperative action.
- CEO scenarios: strategic alliance, channel-exclusive investment, shared data pool, category education.
- output checks: trust threshold, assurance mechanism, staged commitment, exit protection.

#### Chicken / Hawk-Dove / 鹰鸽博弈

- when to use: each side wants the other to yield, and mutual escalation is worst.
- player structure: two players choose aggressive or yielding posture.
- CEO scenarios: public price threat, lawsuit brinkmanship, channel exclusivity standoff, negotiation deadline.
- output checks: escalation cost, face-saving off-ramp, credible commitment, mixed strategy or de-escalation path.

#### Battle Of The Sexes / Preference-Misaligned Coordination / 偏好错位协调

- when to use: players want coordination but prefer different coordinated outcomes.
- player structure: parties agree coordination matters but disagree on standard or venue.
- CEO scenarios: platform API standards, partner roadmap, channel lead ownership, integration priorities.
- output checks: side payments, rotation, governance rule, focal-point creation.

#### Matching Pennies / 猜硬币博弈

- when to use: predictability is bad because one side wins by matching or mismatching the other.
- player structure: two players with directly opposed prediction incentives.
- CEO scenarios: bid shading, promotion timing, competitive intelligence, adversarial channel targeting.
- output checks: recommend randomness, information control, and anti-pattern detection.

### Dynamic And Commitment Games

#### Entry Deterrence / 进入威慑

- when to use: incumbent threatens retaliation to prevent entry.
- player structure: entrant, incumbent, sometimes channel or regulator.
- CEO scenarios: entering a market, launching a new product, opening a new geography.
- output checks: whether threat is credible after entry, incumbent retaliation cost, entrant outside option, subgame-perfect outcome.

#### Commitment Game / 承诺博弈

- when to use: a player changes future incentives by making a costly, visible, hard-to-reverse move.
- player structure: sender of commitment and players who must believe it.
- CEO scenarios: channel exclusivity, capacity buildout, long-term price promise, public roadmap, compliance posture.
- output checks: costliness, observability, reversibility, incentive fit, capability backing.

#### Subgame Perfect Equilibrium / 子博弈精炼均衡

- when to use: threats or promises occur in a sequential game.
- player structure: players move over time and later choices must remain rational.
- CEO scenarios: price-war threat, acquisition walk-away threat, regulator escalation, supplier punishment.
- output checks: apply backward induction and remove threats that would be irrational when reached.

#### Backward Induction / 逆向归纳

- when to use: a finite sequence of moves has clear later-stage choices.
- player structure: decision tree with known order.
- CEO scenarios: staged negotiation, bid escalation, launch-response-retaliation sequence.
- output checks: solve from the last move backward; identify where early commitments alter later incentives.

#### War Of Attrition / 消耗战

- when to use: players compete by waiting or absorbing losses until one gives up.
- player structure: players can endure cost over time.
- CEO scenarios: subsidy battle, litigation endurance, capital-intensive market entry, discount war.
- output checks: cash runway, endurance asymmetry, exit cost, signal of resolve, stopping rule.

#### Hold-Up Problem / 敲竹杠问题

- when to use: one party must invest before another can exploit dependence.
- player structure: investor and counterparty with later bargaining power.
- CEO scenarios: custom integration, channel-specific tooling, platform dependency, supplier-specific capex.
- output checks: asset specificity, contract protection, staged investment, credible exit.

### Market Competition Models

#### Bertrand Competition / 伯特兰价格竞争

- when to use: price is the main strategic variable and products are close substitutes.
- player structure: firms choose prices.
- CEO scenarios: SaaS price cuts, commodity products, agency pricing, marketplace take-rate competition.
- output checks: ability to match price, marginal cost floor, differentiation, customer switching cost, repeated-game discipline.

#### Cournot Competition / 古诺产量竞争

- when to use: quantity or capacity is the main strategic variable.
- player structure: firms choose output or capacity.
- CEO scenarios: supply allocation, manufacturing capacity, ad inventory, logistics slots.
- output checks: capacity constraint, residual demand, rival output reaction, margin impact.

#### Stackelberg Competition / 斯塔克伯格领导者竞争

- when to use: one player moves first and followers react.
- player structure: leader and follower.
- CEO scenarios: capacity precommitment, public pricing architecture, platform rule setting, geographic expansion.
- output checks: first-mover commitment, follower best response, risk of overcommitment.

#### Hotelling / Spatial Differentiation / 霍特林定位差异化

- when to use: positioning and differentiation determine competition.
- player structure: firms choose product, geography, segment, or brand position.
- CEO scenarios: high-end vs low-end positioning, feature differentiation, channel segmentation.
- output checks: customer segments, switching cost, distance from competitor, risk of converging to the middle.

#### Limit Pricing / 限制性定价

- when to use: incumbent prices low to signal low cost or deter entry.
- player structure: incumbent, potential entrant.
- CEO scenarios: category leader lowering price before new entrant, enterprise vendor discounting heavily.
- output checks: cost signal credibility, entrant belief update, short-term profit sacrifice, legal review.

### Information, Signaling, And Screening

#### Bayesian Game / 贝叶斯博弈

- when to use: players have private types, hidden costs, hidden quality, or uncertain willingness to fight.
- player structure: player types, beliefs, strategies by type.
- CEO scenarios: competitor cost uncertainty, investor quality screening, supplier reliability, regulator enforcement probability.
- output checks: type space, prior belief, signals, posterior belief, best response by type.

#### Signaling Game / 信号博弈

- when to use: informed player takes an observable action to influence beliefs.
- player structure: sender with private information and receiver who updates beliefs.
- CEO scenarios: free version announcement, public roadmap, hiring spree, capex commitment, compliance pledge.
- output checks: costly-to-fake test, pooling vs separating signal, receiver action, disconfirmation trigger.

#### Cheap Talk / 廉价谈话

- when to use: messages are costless and non-binding.
- player structure: sender and receiver with partially aligned or misaligned interests.
- CEO scenarios: competitor public statements, negotiation posture, partner promises, investor narrative.
- output checks: incentive alignment, verifiability, history of truthfulness, whether receiver should ignore or discount.

#### Screening / 筛选机制

- when to use: uninformed party designs options to reveal private information.
- player structure: principal offers menu; agents self-select.
- CEO scenarios: pricing tiers, channel partner programs, financing covenants, vendor qualification.
- output checks: self-selection logic, incentive compatibility, adverse selection, exclusion risk.

#### Adverse Selection / 逆向选择

- when to use: hidden quality or type causes bad counterparties to dominate.
- player structure: informed sellers or buyers and uninformed counterparty.
- CEO scenarios: channel recruiting, marketplace supply quality, financing investors, M&A target quality.
- output checks: screening mechanism, warranty, reputation signal, minimum standard.

#### Moral Hazard / 道德风险

- when to use: behavior after agreement is hard to observe or enforce.
- player structure: principal and agent.
- CEO scenarios: channel effort, sales incentive design, outsourcing, post-merger integration.
- output checks: monitoring, incentive alignment, clawbacks, repeated relationship, measurable outcomes.

### Repeated And Evolutionary Games

#### Repeated Game / 重复博弈

- when to use: the same players interact repeatedly and future value changes current incentives.
- player structure: recurring counterparties with memory and punishment options.
- CEO scenarios: channel cooperation, pricing discipline, supplier quality, platform governance.
- output checks: discount factor, future surplus, punishment credibility, reputation, end-game risk.

#### Tit-For-Tat / Reciprocity / 以牙还牙与互惠

- when to use: cooperation can be sustained by matching the other party's previous behavior.
- player structure: repeated bilateral relationship.
- CEO scenarios: channel support, partner co-marketing, supplier service levels.
- output checks: clarity of defection, proportional response, forgiveness rule, noise tolerance.

#### Grim Trigger / 冷酷触发策略

- when to use: one defection causes permanent punishment.
- player structure: repeated relationship with severe punishment.
- CEO scenarios: channel betrayal, data misuse, exclusive partnership breach.
- output checks: severity, credibility, accidental defection risk, whether permanent punishment is too costly.

#### Reputation Game / 声誉博弈

- when to use: current action shapes beliefs in future interactions.
- player structure: current counterparties plus future observers.
- CEO scenarios: regulator communication, customer refunds, partner fairness, acquisition negotiations.
- output checks: audience, signal durability, consistency, long-term trust payoff.

#### Evolutionary Game / 演化博弈

- when to use: strategies spread or disappear across populations over time.
- player structure: many agents using different strategies.
- CEO scenarios: marketplace seller behavior, channel norms, developer ecosystem incentives.
- output checks: fitness/payoff by strategy, adoption dynamics, intervention to shift norms.

### Bargaining, Auctions, And Mechanism Design

#### Nash Bargaining / 纳什谈判

- when to use: parties split surplus and outside options matter.
- player structure: two or more bargainers with disagreement payoff.
- CEO scenarios: financing valuation, M&A terms, revenue share, channel take rate.
- output checks: surplus, BATNA, disagreement payoff, bargaining power, concession path.

#### Ultimatum Game / 最后通牒博弈

- when to use: one side makes take-it-or-leave-it offer and fairness affects acceptance.
- player structure: proposer and responder.
- CEO scenarios: final financing term, acquisition bid, supplier ultimatum, channel exclusivity.
- output checks: responder acceptance threshold, fairness perception, relationship damage, fallback.

#### Rubinstein Alternating-Offer Bargaining / 轮流出价谈判

- when to use: negotiation has repeated offers and delay costs.
- player structure: parties alternate offers over time.
- CEO scenarios: financing rounds, enterprise contract negotiation, M&A exclusivity.
- output checks: patience, deadline, cost of delay, concession schedule, walk-away point.

#### Auction / Bidding Game / 拍卖与竞价博弈

- when to use: players bid for scarce asset or contract.
- player structure: seller/procurer and multiple bidders.
- CEO scenarios: M&A auction, procurement tender, ad bidding, scarce channel slot.
- output checks: auction format, private value vs common value, bid cap, winner's curse, information leakage.

#### Winner's Curse / 赢家诅咒

- when to use: winning may mean overestimating common value.
- player structure: multiple bidders with noisy estimates.
- CEO scenarios: M&A竞价, media rights, land, talent bidding, enterprise procurement.
- output checks: independent valuation, synergy realism, walk-away price, post-win regret.

#### Mechanism Design / 机制设计

- when to use: we design rules so self-interested players reveal information or take desired actions.
- player structure: rule designer and participating agents.
- CEO scenarios: marketplace ranking, sales comp, partner tiering, procurement scoring, platform governance.
- output checks: incentive compatibility, participation constraint, manipulation risk, monitoring burden.

#### VCG / Truthful Mechanism Lens / VCG 与真实揭示机制

- when to use: truthful revelation is critical and participants can manipulate bids or claims.
- player structure: mechanism participants with private valuations.
- CEO scenarios: internal resource allocation, ad auction design, marketplace allocation.
- output checks: truthfulness, budget impact, complexity, user understanding.

### Cooperative, Coalition, And Network Games

#### Coalition Game / 联盟博弈

- when to use: players can form alliances that change payoffs.
- player structure: multiple players and possible coalitions.
- CEO scenarios: channel alliance, platform ecosystem, standards body, M&A consortium.
- output checks: coalition value, blocking coalition, stability, side payments, defection risk.

#### Core / 核心

- when to use: test whether an allocation is stable against subgroup defection.
- player structure: cooperative groups can leave and form alternatives.
- CEO scenarios: revenue share among partners, consortium economics, platform ecosystem rules.
- output checks: no subgroup can do better by leaving; if core is empty, redesign allocation.

#### Shapley Value / 夏普利值

- when to use: allocate surplus by marginal contribution.
- player structure: multiple contributors to joint value.
- CEO scenarios: partner revenue split, data contribution, co-selling economics, joint product bundle.
- output checks: contribution order, marginal value, fairness, implementability.

#### Network Game / 网络博弈

- when to use: payoff depends on who is connected to whom.
- player structure: nodes, links, and externalities.
- CEO scenarios: platform ecosystem, referral network, channel graph, developer marketplace.
- output checks: central nodes, network externalities, tipping risk, intervention point.

#### Multi-Sided Platform Game / 多边平台博弈

- when to use: one side's behavior affects another side's value.
- player structure: platform, supply side, demand side, complementors, regulators.
- CEO scenarios: marketplace fee, app ecosystem, creator platform, channel platform.
- output checks: cross-side network effects, subsidy side, governance rules, disintermediation risk.

### Public Goods, Commons, And Collective Action

#### Public Goods Game / 公共品博弈

- when to use: everyone benefits from contribution but each player prefers others to pay.
- player structure: group of contributors and beneficiaries.
- CEO scenarios: category education, open standards, shared compliance infrastructure, industry lobbying.
- output checks: contribution mechanism, free-rider risk, enforcement, matching funds, governance.

#### Tragedy Of The Commons / 公地悲剧

- when to use: individual usage depletes shared resource.
- player structure: many users of shared capacity or trust.
- CEO scenarios: marketplace quality, channel overuse, shared support resources, brand safety.
- output checks: usage rights, monitoring, quota, pricing, sanction.

#### Volunteer’s Dilemma / 志愿者困境

- when to use: one actor must bear cost for group benefit and everyone hopes someone else acts.
- player structure: multiple beneficiaries; one or few contributors needed.
- CEO scenarios: industry standard maintenance, ecosystem incident response, regulatory self-policing.
- output checks: assignment rule, rotating duty, reward, escalation if nobody volunteers.

### Behavioral And Practical Strategy Lenses

#### Prospect / Loss-Aversion Lens / 前景理论与损失厌恶镜头

- when to use: counterparties react more strongly to losses than equivalent gains.
- player structure: decision makers with behavioral preferences.
- CEO scenarios: price increases, benefit cuts, channel margin reductions, employee negotiation.
- output checks: reference point, perceived loss, framing, staged transition.

#### Fairness And Reciprocity Lens / 公平与互惠镜头

- when to use: acceptance depends on perceived fairness, not just monetary payoff.
- player structure: bargainers or partners with relationship concerns.
- CEO scenarios: channel take rate, supplier terms, post-merger integration, employee equity.
- output checks: fairness benchmark, retaliation risk, transparent rationale, face-saving design.

#### Bounded Rationality Lens / 有限理性镜头

- when to use: players cannot calculate full equilibrium or operate with heuristics.
- player structure: humans or organizations with limited attention and noisy data.
- CEO scenarios: fast-moving competitor response, channel confusion, customer adoption.
- output checks: likely heuristic, salience, decision speed, simplifying signal.

## Output Checklist For Framework Selection

Every report using this catalog should state:

- primary framework selected
- secondary lenses used
- why excluded famous frameworks do not fit
- player structure
- strategy set
- payoff basis and data status
- predicted opponent reactions
- equilibrium or stability interpretation
- credible commitment and signal verdict
- dynamic update triggers
