TITLE_ABBRS = {'Mr', 'Mrs', 'Dr', 'Ms', 'Prof', 'Sen', 'Rep', 'Dr', 'Gen', 'Gov',
                   'Lt', 'Prof', 'Adm', 'Rev', 'Sens', 'Messrs', 'Reps', 'Col', 'St',
                   'Maj', 'M.D', 'Capt', 'Sgt', 'Capt'}
NOT_TITLE = {'While', 'But', 'Speaker', 'American','Father', 'AND', 'Namibian', 'African',
             'Affairs'}

SENTENCE_STARTER =  set(w.title() for w in [
'secondly', 'all', 'consider', 'four', 'finally',
'those', 'under', 'presently', 'returning', 'every', 'founded',
'fearing', 'ten', 'past', 'further', 'situated', 'even', 'what',
'near', 'current', 'scientists', 'notable', 'here', 'let', 'others',
'along', 'legend', 'later', 'prior', 'usually', 'regardless',
'besides', 'suddenly', 'opponents', 'from', 'two', 'next', 'and',
'therefore', 'until', 'today', 'more', 'supporters', 'it', 'none', 'this',
'local', 'originally', 'following', 'my', 'rather', 'six',
'located', 'occasionally', 'instead', 'plans', 'critics', 'earlier',
'membership', 'such', 'a', 'whenever', 'subsequently', 'typical',
'over', 'soon', 'whilst', 'through', 'still', 'its', 'symptoms',
'main', 'then', 'males', 'they', 'arriving', 'now', 'tourism', 'each',
'everyone', 'owing', 'our', 'beyond', 'ultimately', 'furthermore', 'since',
'she', 'after', 'given', 'beginning', 'hence', 'major', 'thereafter',
'one', 'another', 'little', 'sadly', 'similarly', 'accordingly',
'approximately', 'their', 'luckily', 'unfortunately', 'patients',
'contrary', 'modern', 'apparently', 'traditionally', 'depending', 'aside',
'note', 'finding', 'so', 'ironically', 'towards', 'unless', 'though',
'visitors', 'eight', 'but', 'neighboring', 'professor', 'traditional',
'construction', 'typically', 'based', 'only',
'believing', 'indeed', 'thousands', 'his', 'meanwhile', 'overall', 'nearly',
'despite', 'during', 'common', 'proponents', 'inside', 'see', 'subsequent',
'currently', 'please', 'yet', 'outside', 'unable', 'various', 'between',
'neither', 'before', 'numerous', 'knowing', 'we', 'recently', 'initially',
'however', 'historians', 'article', 'hundreds', 'both', 'essentially', 'many',
'taking', 'according', 'players', 'nearby', 'among', 'afterwards', 'whatever',
'moreover', 'throughout', 'considering', 'angel', 'three', 'much', 'certain',
'an', 'former', 'unlike', 'these', 'mount', 'while',
'suppose', 'seven', 'eventually', 'almost', 'thus', 'surprisingly', 'in',
'if', 'perhaps', 'realizing', 'several', 'upon', 'recent', 'shortly',
'nevertheless', 'nonetheless', 'hispanic', 'without', 'the', 'otherwise',
'researchers', 'just', 'generally', 'nicknamed', 'thanks', 'immediately',
'previous', 'adding', 'also', 'except', 'around', 'early', 'five',
'using', 'apart', 'apple', 'like', 'alternatively', 'because',
'often', 'some', 'born', 'examples', 'gradually', 'for', 'assuming',
'continuing', 'notably', 'although', 'by', 'on', 'about', 'most',
'emperor', 'consequently', 'seeing', 'firstly', 'formerly', 'previously',
'within', 'due', 'references', 'lastly', 'nowadays', 'additional', 'her',
'there', 'specifically', 'naturally', 'elsewhere', 'amongst',
'with', 'he', 'whether', 'vacancies', 'official', 'historically',
'below', 'similar', 'sometimes', 'adults', 'likewise', 'general',
'as', 'sometime', 'at', 'again', 'compared', 'no', 'whereas', 'when',
'members', 'other', 'users', 'reportedly', 'students',
'additionally', 'source', 'normally', 'together', 'having', 'starting',
'once'
])