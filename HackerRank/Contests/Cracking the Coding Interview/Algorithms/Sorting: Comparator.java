// Write your Checker class here
class Checker implements Comparator<Player>{

	@Override
	public int compare(Player o1, Player o2) {
		// TODO Auto-generated method stub
		Integer result = Integer.valueOf(o1.score).compareTo(o2.score);
		
		if(result == 0){
			return o1.name.compareTo(o2.name);
		}else{
			return result  * -1;
		}
	}
	
}
