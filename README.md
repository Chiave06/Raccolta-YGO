# Raccolta carte: Yu-Gi-Oh!, Pokémon, Magic

Un sito personale per tenere traccia delle tue carte e non comprarle due volte. Per ogni carta salvi nome, codice, espansione, rarità, edizione (o finitura per Magic), lingua e copie. Ci sono una lista dei desideri, il controllo "Ce l'ho già?", i suggerimenti mentre scrivi, la modifica delle carte già registrate, l'esportazione in CSV e il menu **Italiano / English**.

È un sito statico: funziona su GitHub Pages senza server.

## Cosa c'è nella cartella

| File | A cosa serve |
|---|---|
| `index.html` | Pagina Yu-Gi-Oh! |
| `pokemon.html` | Pagina Pokémon |
| `magic.html` | Pagina Magic |
| `cards.json`, `pokemon.json`, `magic.json` | Elenchi di carte per i suggerimenti (`magic.json` compare dopo la prima esecuzione dell'azione automatica) |
| `tools/make_db.py`, `tools/make_pkm_db.py`, `tools/make_mtg_db.py` | Script che rigenerano i tre elenchi dai dati pubblici |
| `.github/workflows/update-cards.yml` | Azione che aggiorna gli elenchi ogni lunedì |
| `LICENSE`, `NOTICE.md` | Licenza del codice, fonti dei dati, marchi e crediti |

## 1. Mettere online il sito

1. Su GitHub crea un repository **pubblico**, per esempio `raccolta-carte` (Pages sui repository privati richiede un piano a pagamento).
2. Carica i file con **Add file → Upload files**: `index.html`, `pokemon.html`, `magic.html`, `cards.json`, `pokemon.json`, `LICENSE`, `NOTICE.md`, `README.md` e la cartella `tools`. Poi **Commit changes**.
3. Crea a mano il file dell'azione, perché le cartelle che iniziano con un punto a volte non vengono caricate: **Add file → Create new file**, come nome scrivi `.github/workflows/update-cards.yml` (le barre creano le cartelle), incolla il contenuto del file con lo stesso nome e premi **Commit changes**.
4. Vai in **Settings → Pages**. Alla voce *Build and deployment* scegli *Deploy from a branch*, ramo `main`, cartella `/ (root)`, poi **Save**.
5. Dopo uno o due minuti il sito è su `https://TUONOME.github.io/NOME-REPOSITORY/`.

Per aggiornare il sito in futuro basta sostituire i file `.html` con quelli nuovi.

## 2. Aggiornare gli elenchi delle carte

L'azione **Aggiorna elenchi carte** scarica i dati delle tre fonti, rigenera i tre file `.json` e li salva solo se ci sono novità. Parte da sola ogni lunedì mattina.

- **Provala subito:** scheda **Actions** → *Aggiorna elenchi carte* → **Run workflow**. La prima volta crea `magic.json`; il passaggio di Magic scarica un file grosso e può durare qualche minuto. Finché `magic.json` non esiste, nella pagina Magic le carte si inseriscono a mano.
- **Se qualcosa non va:** apri l'esecuzione, clicca su **aggiorna** a sinistra e guarda il passaggio con la croce rossa. I tre giochi sono indipendenti: se uno fallisce, gli altri si aggiornano lo stesso.
- Se l'azione non riesce a salvare, vai in **Settings → Actions → General → Workflow permissions** e scegli *Read and write permissions*.
- GitHub sospende le azioni programmate dopo 60 giorni senza attività nel repository. Se succede, riattivala dalla scheda Actions.
- Nel sito, il pulsante **Aggiorna elenco carte** carica l'ultima versione senza ricaricare la pagina e mostra la data dell'elenco.
- Un'espansione appena uscita può comparire con qualche giorno di ritardo, perché dipende dalle fonti.

**Attenzione per Pokémon:** la fonte (PokemonTCG/pokemon-tcg-data) è dichiarata obsoleta e l'API collegata è prevista offline dal 1 marzo 2027. Il sito continuerà a funzionare con l'elenco già scaricato, ma dopo quella data non riceverà nuove espansioni e le immagini caricate da pokemontcg.io potrebbero non comparire più.

## 3. Usare la raccolta da più dispositivi

Senza collegamento, le carte restano nella memoria del browser, separate per gioco. Se svuoti i dati del browser o cambi dispositivo, non ci sono più.

Per ritrovarle ovunque, in fondo a ogni pagina c'è il riquadro **Altri dispositivi**. Collega un secondo repository, **privato**, che contiene le tre raccolte (`collection.json`, `collection-pkm.json`, `collection-mtg.json`).

1. Crea un repository privato, per esempio `ygo-dati`, con l'opzione *Add a README file*.
2. Vai in **Settings (del tuo profilo) → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**. Come accesso scegli *Only select repositories* e solo `ygo-dati`. Nei permessi del repository imposta **Contents: Read and write**. Scegli una scadenza.
3. Nel sito scrivi `tuonome/ygo-dati`, incolla il token e premi **Collega e sincronizza**. Il collegamento vale per tutte e tre le pagine.
4. Sugli altri dispositivi apri il sito e ripeti il passaggio 3.

Come funziona:
- Ogni modifica parte da sola dopo pochi secondi; **Sincronizza ora** la forza.
- Se due dispositivi cambiano la stessa carta, vince la modifica più recente.
- Il token è salvato solo nel browser di quel dispositivo. Usa un token limitato a `ygo-dati`, così non dà accesso ad altro.
- **Esporta CSV** e **Importa CSV** servono per una copia di sicurezza o per spostare i dati.

## Limiti da conoscere

- Le immagini sono caricate dal browser da servizi esterni (vedi `NOTICE.md`): se quei servizi non rispondono, vedi un trattino al posto dell'immagine.
- Pokémon ha solo i nomi inglesi; Yu-Gi-Oh! ha i nomi in sei lingue; Magic usa i nomi inglesi.
- Le carte inserite a mano, senza scegliere dai suggerimenti né digitare un codice presente nell'elenco, non hanno immagine.
- I Token di Yu-Gi-Oh! non sono nell'elenco e vanno inseriti a mano.

## Licenza e crediti

Il codice è sotto licenza **MIT** (`LICENSE`). I dati e le immagini delle carte appartengono ai rispettivi titolari e provengono dalle fonti elencate in `NOTICE.md`. Il progetto non è affiliato a Konami, Nintendo, Creatures, GAME FREAK, Wizards of the Coast, YGOPRODeck, pokemontcg.io o Scryfall.
